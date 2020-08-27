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

import os
import shutil
from termcolor import colored
from storm.parameters import get_supported_theories
from storm.parameters import get_parameters_dict

def get_all_smt_files_recursively(path_to_directory):
    file_paths = list()
    for r, d, f in os.walk(path_to_directory):
        for file in f:
            if ".smt20" in file:
                continue
            if ".smt2" in file:
                file_paths.append(os.path.join(r,file))

    return file_paths


def create_smt2_file(path, string):
    file = open(path, "w")
    file.write(string)
    file.close()

def create_file(data, path):
    file = open(path, "w")
    file.write(data)
    file.close()

def append_row(data, path):
    file = open(path, "a")
    file.write(data + "\n")
    file.close()


def create_server_core_directory(temp_dir, server, core):
    if not os.path.exists(temp_dir):
        try:
            os.mkdir(temp_dir)
        except:
            pass
    server_dir = os.path.join(temp_dir, server)
    core_dir = os.path.join(server_dir, "core_" + str(core))
    if not os.path.exists(server_dir):
        os.mkdir(server_dir)

    if os.path.exists(core_dir):
        shutil.rmtree(core_dir)
        os.mkdir(core_dir)
    else:
        os.mkdir(core_dir)
    print("####### [Created core dir] - " + core_dir )
    return core_dir


def get_mutant_paths(temp_dir):
    mutant_paths = list()
    for r, d, f in os.walk(temp_dir):
        mutant_paths = [os.path.join(temp_dir, i) for i in f]
        break
    return mutant_paths


def refresh_directory(dir_path):
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)
        os.mkdir(dir_path)


def pick_a_supported_theory(path_to_benchmark, solver, seed):
    import random
    random.seed(seed)
    all_theories_in_benchamark_dir = os.listdir(path_to_benchmark)
    while True:
        theory = random.choice(all_theories_in_benchamark_dir)
        if theory in get_supported_theories(solver):
            return theory


def record_soundness(home_directory, seed_file_path, buggy_mutant_path, seed, mutant_number, seed_theory, fuzzing_parameters):
    temp_dir = os.path.join(home_directory, "temp")
    print(colored("Creating a soundness folder at: ", "magenta", attrs=["bold"]) + temp_dir)
    print(colored("seed file path: ", "magenta", attrs=["bold"]) + seed_file_path)
    print(colored("buggy mutant file path: ", "magenta", attrs=["bold"]) + buggy_mutant_path)
    # check if the soundness folder exists
    path_to_soundness_folder = os.path.join(temp_dir, "soundness")
    number_of_directories = 0
    for r, d, f in os.walk(path_to_soundness_folder):
        number_of_directories = len(d)
        break

    if not os.path.exists(path_to_soundness_folder):
        os.mkdir(path_to_soundness_folder)

    # Create a directory for the bug
    path_to_bug_dir = os.path.join(path_to_soundness_folder, str(number_of_directories))
    os.mkdir(path_to_bug_dir)

    # copy the orig file and the mutant to the directory for the bug
    shutil.copy2(seed_file_path, path_to_bug_dir)
    shutil.copy2(buggy_mutant_path, path_to_bug_dir)

    error_logs = "Some info on this bug:\n"
    error_logs += "seed to run_storm() function: " + str(seed) + "\n"
    error_logs += "Path to original file: " + seed_file_path + "\n"
    error_logs += "This was the [" + str(mutant_number) + "]th mutant\n"
    error_logs += "Seed theory: " + seed_theory + "\n"
    error_logs += "\nConfiguration: " + "\n"
    error_logs += str(fuzzing_parameters)
    error_logs += "\n"

    create_file(error_logs, os.path.join(path_to_bug_dir, "error_logs.txt"))
