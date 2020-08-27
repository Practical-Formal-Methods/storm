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

import argparse
import multiprocessing
import time
from termcolor import colored
from storm.fuzzer.fuzzer import generate_mutants
from storm.fuzzer.helper_functions import add_check_sat_using, insert_pushes_pops
from storm.minimizer.minimizer import minimize
from storm.runner.solver_runner import solver_runner
from storm.smt.smt_object import smtObject
from storm.utils.file_operations import get_all_smt_files_recursively, create_server_core_directory, refresh_directory, \
    get_mutant_paths, pick_a_supported_theory, record_soundness
from storm.parsers.argument_parser import MainArgumentParser
from storm.utils.max_depth import get_max_depth, count_asserts, count_lines
from storm.utils.randomness import Randomness
from storm.config import config
from z3 import *
from storm.parameters import get_parameters_dict
import shutil
from storm.utils.file_operations import append_row
import time


ALL_FUZZING_PARAMETERS = None


def run_storm(parsedArguments, core, SEED, wait, reproduce, rq3, fuzzing_params):

    def run_mutants_in_a_thread(path_to_temp_core_directory, signal, seed_file_number, seed_file_path, incrementality, solver, fuzzing_parameters):
        mutant_file_paths = get_mutant_paths(path_to_temp_core_directory)
        mutant_file_paths.sort()
        if len(mutant_file_paths) > 0:
            if signal == 1:
                print(colored("\tExperienced timeout while exporting mutants. But we still were able to export some",
                              "magenta", attrs=["bold"]))
            print("####### RUNNING MUTANTS")
            start_time = time.time()
            for i, mutant_path in enumerate(mutant_file_paths):
                output = solver_runner(solver_path=parsedArguments["solverbin"],
                                       smt_file=mutant_path,
                                       temp_core_folder=path_to_temp_core_directory,
                                       timeout=ALL_FUZZING_PARAMETERS["solver_timeout"],
                                       incremental=incrementality,
                                       solver = solver)
                print("[" + parsedArguments["solver"] +"]\t"+ "[core: " + str(core) +"]\t", end="")
                print("[seed_file: " + str(seed_file_number) +"]\t\t" + "[" + str(i+1) + "/" + str(len(mutant_file_paths)) + "]\t\t", end="")
                print("[" + parsedArguments["theory"] +"]\t", end="")

                if output == "sat":
                    print(colored(output, "green", attrs=["bold"]))
                elif output == "unsat":
                    print(colored(output, "red", attrs=["bold"]))
                    print(mutant_path)
                    print(colored("SOUNDNESS BUG", "white", "on_red", attrs=["bold"]))
                    print("SEED = " + str(SEED))
                    # Handle unsoundness
                    record_soundness(home_directory=config["home"],
                                     seed_file_path=seed_file_path,
                                     buggy_mutant_path=mutant_path,
                                     seed=SEED,
                                     mutant_number=i,
                                     seed_theory=parsedArguments["theory"],
                                     fuzzing_parameters=fuzzing_parameters)
                    print(colored("Time to bug: ", "magenta", attrs=["bold"]) + str(time.time() - start_time))
                    print(colored("Iterations to bug: ", "magenta", attrs=["bold"]) + str(i+1))
                elif output == "error":
                    print(colored(output, "white", "on_red", attrs=["bold"]))
                else:
                    print(colored(output, "yellow", attrs=["bold"]))
                os.remove(mutant_path)  # remove mutant when processed


    """
        Initalizations
    """
    time.sleep(wait)
    print("Running storm on a core")
    temp_directory = os.path.join(config["home"], "temp")
    path_to_temp_core_directory = os.path.join(temp_directory, parsedArguments["server"], "core_" + core)
    create_server_core_directory(temp_directory, parsedArguments["server"], core)
    seed_file_paths = []

    global ALL_FUZZING_PARAMETERS
    if not reproduce:
        # normal mode
        ALL_FUZZING_PARAMETERS = get_parameters_dict(replication_mode = False,
                                                     bug_number=None)
        path_to_theory = os.path.join(parsedArguments["benchmark"], parsedArguments["theory"])
        if not os.path.exists(path_to_theory):
            print(colored("Theory not found in the benchmarks folder", "red"))
            return 1
        seed_file_paths = get_all_smt_files_recursively(path_to_theory)
    else:
        # FSE2020 bugs reproduction mode
        # Get the path to the seed file
        ALL_FUZZING_PARAMETERS = get_parameters_dict(replication_mode=True,
                                                     bug_number=parsedArguments["reproduce"])
        path_to_seed_file = os.path.join(config["home"], "storm", "fse_repl", parsedArguments["reproduce"], "seed.smt2")
        print("Path to seed file for this bug = " + path_to_seed_file)
        seed_file_paths.append(path_to_seed_file)
        parsedArguments["theory"] = ALL_FUZZING_PARAMETERS["theory"]


    randomness = Randomness(SEED)
    randomness.shuffle_list(seed_file_paths)
    # run the file and see if it is SAT or UNSAT
    for i, file in enumerate(seed_file_paths):
        # Refresh core directory
        refresh_directory(path_to_temp_core_directory)
        incrementality = randomness.random_choice(ALL_FUZZING_PARAMETERS["incremental"])
        print("####### [" + str(i) + "] seed: ", end="")
        smt_Object = smtObject(file_path=file, path_to_mutant_folder=path_to_temp_core_directory)
        if not smt_Object.get_validity():
            print(colored("Was not able to parse the smt file", "red"))
            return 1

        smt_Object.check_satisfiability(timeout=ALL_FUZZING_PARAMETERS["solver_timeout"])
        if smt_Object.get_orig_satisfiability() == "timeout":
            continue
        if not smt_Object.get_validity():
            continue

        max_depth = ALL_FUZZING_PARAMETERS["max_depth"]
        max_assert = ALL_FUZZING_PARAMETERS["max_assert"]

        # Generate all mutants at once for this file in a thread with a timeout
        signal = generate_mutants(smt_Object=smt_Object,
                                  path_to_directory=path_to_temp_core_directory,
                                  maxDepth=max_depth,
                                  maxAssert=max_assert,
                                  seed=SEED,
                                  theory=parsedArguments["theory"],
                                  fuzzing_parameters=ALL_FUZZING_PARAMETERS)
        mutant_file_paths = get_mutant_paths(path_to_temp_core_directory)

        if len(mutant_file_paths) == 0:
            print(colored("NO MUTANTS GENERATED", "red", attrs=["bold"]))
            continue

        # Incremental setting apply to all mutants of a file
        print("####### Setting incrementality with prob: " + colored(str(ALL_FUZZING_PARAMETERS["incremental"]), "yellow", attrs=["bold"]))
        print("####### Incrementality: ", end="")
        if incrementality == "yes":
            print(colored("YES", "green", attrs=["bold"]))
            mutant_file_paths.sort()
            insert_pushes_pops(mutant_file_paths, randomness)
        else:
            print(colored("NO", "red", attrs=["bold"]))


        print("####### Adding check-sat-using options with prob: " + colored(str(ALL_FUZZING_PARAMETERS["check_sat_using"]), "yellow", attrs=["bold"]))
        for mutant_file_path in mutant_file_paths:
            if randomness.random_choice(ALL_FUZZING_PARAMETERS["check_sat_using"]) == "yes" and parsedArguments["solver"] == "z3":
                check_sat_using_option = randomness.random_choice(ALL_FUZZING_PARAMETERS["check_sat_using_options"])
                add_check_sat_using(mutant_file_path, check_sat_using_option)


        # If we are in bug repoduction mode, copy the buggy mutant to the bug folder in fse replication folder
        if reproduce:
            print("copying the buggy mutant")
            buggy_mutant = [i for i in mutant_file_paths if i.find(ALL_FUZZING_PARAMETERS["buggy_mutant"]) != -1][0]
            path_to_bug_directory_in_fse_repl = os.path.join(config["home"], "storm", "fse_repl", parsedArguments["reproduce"])
            print(colored("copying the buggy mutant to: ", "yellow", attrs=["bold"]) + path_to_bug_directory_in_fse_repl)
            shutil.copy2(buggy_mutant, path_to_bug_directory_in_fse_repl)
            if parsedArguments["solverbin"] is None:
                print("Skipping mutant running since --solverbin and --solver flags are None")
                continue

        # Spawn a new process and run mutants
        process = multiprocessing.Process(target=run_mutants_in_a_thread, args=(path_to_temp_core_directory,
                                                                                signal,
                                                                                i,
                                                                                file,
                                                                                incrementality,
                                                                                parsedArguments["solver"],
                                                                                ALL_FUZZING_PARAMETERS))
        process.start()
        process.join(ALL_FUZZING_PARAMETERS["mutant_running_timeout"])
        if process.is_alive():
            process.terminate()
            print(colored("TIMEOUT WHILE RUNNING THE MUTANTS", "red", attrs=["bold"]))
            time.sleep(ALL_FUZZING_PARAMETERS["solver_timeout"])  # Wait for the solver to finish processing the last file before deleting the temp dir
        refresh_directory(path_to_temp_core_directory)


def main():
    os.system("clear")
    print(colored("############################", "blue", "on_white", attrs=["bold"]))
    print(colored("  Welcome to storm v.1.0.0  ", "blue", "on_white", attrs=["bold"]))
    print(colored("############################", "blue", "on_white", attrs=["bold"]))
    arguments = MainArgumentParser()
    arguments.parse_arguments(argparse.ArgumentParser())
    parsedArguments = arguments.get_arguments()
    print(parsedArguments)

    SEED = parsedArguments["seed"]
    reproduction_mode = True if parsedArguments["reproduce"] is not None else False

    # Minimization mode
    if parsedArguments["min"]:
        if parsedArguments["file_path"] is None:
            print(colored("--file_path argument cannot be None", "red", attrs=["bold"]))
            return 1
        if parsedArguments["solverbin"] is None:
            print(colored("--solverbin argument cannot be None", "red", attrs=["bold"]))
            return 1
        if parsedArguments["solver"] is None:
            print(colored("--solver argument cannot be None", "red", attrs=["bold"]))
            return 1
        if parsedArguments["theory"] is None:
            print(colored("--theory argument cannot be None", "red", attrs=["bold"]))
            return 1

        minimize_dir_path = os.path.dirname(os.path.realpath(parsedArguments["file_path"]))
        stats_file = os.path.join(minimize_dir_path, "min_stats.csv")
        orig_maxDepth = get_max_depth(parsedArguments["file_path"])
        orig_asserts = count_asserts(parsedArguments["file_path"])
        orig_lines = count_lines(parsedArguments["file_path"])
        orig_size = os.path.getsize(parsedArguments["file_path"])
        row_2 = "ORIGINAL,-," + str(orig_maxDepth) + "," + str(orig_asserts) + "," + str(orig_lines) + "," + str(orig_size) + ", ,"
        file = open(stats_file, "w")
        file.writelines("iteration, seed, maxDepth, maxAssert, line_numbers, bytes, number of queries, time\n" + row_2)
        file.close()

        temp_dir = os.path.join(minimize_dir_path, "temp")
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        os.mkdir(temp_dir)

        def minimize_in_parallel(dir_path, file_path, solver_bin, maxDepth, maxAssert, seed, parsed_arguments, iteration):
            minimizer = minimize(dir_path=dir_path,
                                 file_path = file_path,
                                 solverbin=solver_bin,
                                 maxDepth=maxDepth,
                                 maxAssert=maxAssert,
                                 SEED=seed,
                                 parsedArguments=parsed_arguments,
                                 iteration=iteration)

        # Run minimizer in parallel
        if parsedArguments["cores"] is None:
            cores = 1
        else:
            cores = int(parsedArguments["cores"])
        for i in range(cores):
            process = multiprocessing.Process(target=minimize_in_parallel, args=(minimize_dir_path,
                                                                                 parsedArguments["file_path"],
                                                                                 parsedArguments["solverbin"],
                                                                                 64,
                                                                                 64,
                                                                                 i,
                                                                                 parsedArguments,
                                                                                 i))
            process.start()
            os.system("taskset -p -c " + str(i) + " " + str(process.pid))
        return 0


    if not reproduction_mode:
        if parsedArguments["benchmark"] is None:
            print(colored("--benchmark argument cannot be None", "red", attrs=["bold"]))
            return 1
        if parsedArguments["solver"] is None:
            print(colored("--solver argument cannot be None", "red", attrs=["bold"]))
            return 1
        if parsedArguments["solverbin"] is None:
            print(colored("--solverbin argument cannot be None", "red", attrs=["bold"]))
            return 1


    theory_provided = False
    if not parsedArguments["theory"] is None:
        theory_provided = True

    try:
        if parsedArguments["cores"] is not None:
            for i in range(int(parsedArguments["cores"])):
                if not theory_provided and not reproduction_mode:
                    print(colored("--theory argument is None. Automatically selecting theory", "magenta", attrs=["bold"]))
                    parsedArguments["theory"] = pick_a_supported_theory(parsedArguments["benchmark"], parsedArguments["solver"], SEED)
                    print(colored("Picked theory = " + parsedArguments["theory"], "magenta", attrs=["bold"]))
                core = str(i)
                wait = int(parsedArguments["cores"])
                process = multiprocessing.Process(target=run_storm, args=(parsedArguments,core, SEED, wait, reproduction_mode, False, None))
                process.start()
                # pin the process to a specific CPU
                os.system("taskset -p -c " + str(i) + " " + str(process.pid))
                SEED = str((int(SEED) + 1))
        else:
            if not theory_provided and not reproduction_mode:
                print(colored("--theory argument is None. Automatically selecting theory", "magenta", attrs=["bold"]))
                parsedArguments["theory"] = pick_a_supported_theory(parsedArguments["benchmark"], parsedArguments["solver"], SEED)
                print(colored("Picked theory = " + parsedArguments["theory"], "magenta", attrs=["bold"]))
            run_storm(parsedArguments, "0", SEED, 0, reproduction_mode, False, None)

    except (KeyboardInterrupt, SystemExit):
        print("\nGood Bye!\n")


if __name__ == '__main__':
    # export LD_LIBRARY_PATH=/home/numair/Pictures/cudd/cudd/.libs/;export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/numair/Pictures/libpoly/build/src/
    # storm --benchmark=/home/numair/Downloads/smt_benchmarks --solverbin=/home/numair/z3Build/bin/z3 --solver=z3 --server= ??? --theory= ??? --cores= ???

    # Replication
    # If we want to refind a bug with a seed. If we want to find the seed. Use the above command
    # storm --reproduce=bug20 --solverbin= ??? --solver= ??? --server= ??? --cores= ???

    # If we want to only reproduce with a seed and not run it
    # storm --reproduce=bug20 --seed= ???

    # MINIMIZATION:
    # storm --min --file_path= ??? --solver= ??? --solverbin= ??? --theory= ???  --check_sat_using= ??? --incremental[FLAG]
    main()
