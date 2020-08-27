"""
Copyright 2020 MPI-SWS

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from storm.fuzzer.fuzzer import generate_mutants
from storm.fuzzer.helper_functions import insert_pushes_pops, add_check_sat_using
from storm.runner.solver_runner import solver_runner
from storm.smt.smt_object import smtObject
from storm.utils.file_operations import get_mutant_paths
import os
from termcolor import colored
import shutil
import time
from storm.utils.max_depth import get_max_depth
from storm.utils.randomness import Randomness


class minimize(object):
    def __init__(self, dir_path, file_path, solverbin, maxDepth, maxAssert, SEED, parsedArguments, iteration):
        """
            filepath is a path to a dir containing the config file and the buggy mutant
        """
        print(colored("MINIMIZATION MODE", "blue", attrs=["bold"]))
        self.iteration = iteration
        self.stats_file = os.path.join(dir_path, "min_stats.csv")
        self.dir_path = dir_path
        self.temp_dir = os.path.join(dir_path, "temp", str(iteration))
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
        os.mkdir(self.temp_dir)
        self.orig_file_path = file_path
        self.solverbin = solverbin
        self.maxDepth = maxDepth
        self.maxAssert = maxAssert
        self.seed = SEED
        # copy the original mutant and create a file called "minimized.smt2"
        shutil.copy2(self.orig_file_path, os.path.join(dir_path, "minimized_"+ str(iteration) + ".smt2"))
        self.minimized_file_path = os.path.join(dir_path, "minimized_"+ str(iteration) + ".smt2")
        self.incremental = parsedArguments["incremental"]
        self.check_sat_using = parsedArguments["check_sat_using"]
        self.theory = parsedArguments["theory"]
        self.solver = parsedArguments["solver"]
        self.fuzzing_parameters = {
            "enrichment_steps": 1000,
            "number_of_mutants": 1000,
            "mutant_generation_timeout": 1000,
            "mutant_running_timeout": 1800,
            "solver_timeout": 60
        }
        self.randomness = Randomness(self.seed)
        print(colored("Incremental Mode = ", "white", "on_blue", attrs=["bold"]) + colored(str(self.incremental), "yellow", attrs=["bold"]))
        print(colored("check_sat_using = ", "white", "on_blue", attrs=["bold"]) + colored(str(self.check_sat_using), "yellow", attrs=["bold"]))
        print(colored("Theory = ", "white", "on_blue", attrs=["bold"]) + colored(str(self.theory), "yellow", attrs=["bold"]))
        print(colored("Solver = ", "white", "on_blue", attrs=["bold"]) + colored(str(self.solver), "yellow", attrs=["bold"]))
        self.min_depth = None
        self.min_assert = self.count_asserts(self.minimized_file_path)
        self.number_of_queries = 0
        start_time = time.time()
        self.minimizeDepth(0, 64)
        print("Minimum Depth = " + str(self.min_depth))
        self.minimizeAssertions(4, self.min_assert)
        self.minimizeLines(self.min_depth, self.min_assert)
        shutil.rmtree(self.temp_dir)
        file = open(self.stats_file, "a+")
        self.min_lines = self.get_number_of_lines(self.minimized_file_path)
        self.min_bytes = os.path.getsize(self.minimized_file_path)
        max_depth = get_max_depth(self.minimized_file_path)
        end_time = time.time()

        file.writelines("\n" + str(iteration) + "," + str(SEED) + "," + str(max_depth) + "," + str(self.min_assert) +
                        "," + str(self.min_lines) + "," + str(self.min_bytes) + "," + str(self.number_of_queries) + "," +
                        str(end_time - start_time))
        file.close()


    def get_number_of_lines(self, file_path):
        with open(file_path, 'r') as f:
            lines = f.read().splitlines()
        return len(lines)

    def count_asserts(self, file_path):
        number_of_assertions = 0
        with open(file_path, 'r') as f:
            lines = f.read().splitlines()
        for line in lines:
            if line.find("(assert") != -1:
                number_of_assertions += 1
        return number_of_assertions


    def generate_and_run_mutants(self, maxDepth, maxAssert):
        smt_Object = smtObject(file_path=self.minimized_file_path, path_to_mutant_folder=self.temp_dir)
        smt_Object.check_satisfiability(timeout=120)
        signal = generate_mutants(smt_Object=smt_Object, path_to_directory=self.temp_dir, maxDepth=maxDepth, maxAssert=maxAssert,
                                  seed=self.seed, theory=self.theory, fuzzing_parameters=self.fuzzing_parameters)
        mutant_file_paths = get_mutant_paths(self.temp_dir)
        if self.incremental:
            mutant_file_paths.sort()
            insert_pushes_pops(mutant_file_paths, self.randomness)
        for mutant_file_path in mutant_file_paths:
            if self.check_sat_using is not None:
                add_check_sat_using(mutant_file_path, self.check_sat_using)
        # run mutants
        unsat_mutants = []
        running_start = time.time()
        print(colored("Running Mutants.... ", "green", attrs=["bold"]))
        for mutant in mutant_file_paths:
            output = solver_runner(solver_path=self.solverbin, smt_file=mutant, temp_core_folder=self.temp_dir,
                                   timeout=self.fuzzing_parameters["solver_timeout"], incremental="yes" if self.incremental else "no",
                                   solver=self.solver)

            self.number_of_queries += 1
            if output == "unsat":
                unsat_mutants.append(mutant)

            # stop running mutants after 30 mins
            current_time = time.time()
            if (int(current_time - running_start) > self.fuzzing_parameters["mutant_running_timeout"]):
                print(colored(">>> TIMEOUT WHILE RUNNING THE MUTANTS <<<< ", "red", attrs=["bold"]))
                break


        if len(unsat_mutants) > 0:
            min_lines = self.get_number_of_lines(unsat_mutants[0])
            min_mutant = unsat_mutants[0]
            for mutant in unsat_mutants[1:]:
                if self.get_number_of_lines(mutant) < min_lines:
                    min_lines = self.get_number_of_lines(mutant)
                    min_mutant = mutant
            print(colored("Found a failing example", "green", attrs=["bold"]))
            return True, min_mutant
        print(colored("Could not find a failing example with these parameters", "red", attrs=["bold"]))
        return False, ""


    def minimizeLines(self, maxDepth, maxAssert):
        minimum_number_of_lines = self.get_number_of_lines(self.minimized_file_path)
        for i in range(10):
            print(colored("min LINE NUMBERS = " + str(self.get_number_of_lines(self.minimized_file_path)), "magenta", attrs=["bold"]))
            success_flag, mutant = self.generate_and_run_mutants(maxDepth, maxAssert)
            if success_flag and minimum_number_of_lines > self.get_number_of_lines(mutant):
                print(colored("new min LINE NUMBERS = " + str(self.get_number_of_lines(mutant)), "green", attrs=["bold"]))
                minimum_number_of_lines = self.get_number_of_lines(mutant)
                shutil.copy2(mutant, os.path.join(self.dir_path, "minimized_"+ str(self.iteration) + ".smt2"))


    def minimizeDepth(self, minDepth, maxDepth):
        print(colored("DEPTH BOUNDS: minDepth= " + str(minDepth) + ",  maxDepth= " + str(maxDepth) + "   maxAssert= " + str(self.min_assert), "white", "on_blue", attrs=["bold"]))
        if minDepth == maxDepth - 1:
            print(colored("             ", "white", "on_red", attrs=["bold"]))
            print(colored("MIN DEPTH = " + str(maxDepth) + " ", "white", "on_red", attrs=["bold"]))
            print(colored("             ", "white", "on_red", attrs=["bold"]))
            self.min_depth = maxDepth
            return maxDepth
        midpoint = int((minDepth + maxDepth)/2)
        success_flag, mutant = self.generate_and_run_mutants(midpoint, self.min_assert)
        if success_flag:
            shutil.copy2(mutant, os.path.join(self.dir_path, "minimized_"+ str(self.iteration) + ".smt2"))
            self.minimizeDepth(minDepth, midpoint)
        else:
            self.minimizeDepth(midpoint, maxDepth)


    def minimizeAssertions(self, minAssert, maxAssert):
        print(colored("ASSERT BOUNDS: maxDepth=" + str(self.min_depth) + ",   minAssert= " + str(minAssert) + ",  maxAssert= " + str(maxAssert), "white", "on_blue", attrs=["bold"]))
        if minAssert == maxAssert - 1:
            self.min_assert = maxAssert
            return maxAssert
        midpoint = int((minAssert + maxAssert) / 2)
        success_flag, mutant = self.generate_and_run_mutants(self.min_depth, midpoint)
        if success_flag:
            shutil.copy2(mutant, os.path.join(self.dir_path, "minimized_"+ str(self.iteration) + ".smt2"))
            min_assert = self.minimizeAssertions(minAssert, midpoint)
        else:
            min_assert =self.minimizeAssertions(midpoint, maxAssert)
        return min_assert