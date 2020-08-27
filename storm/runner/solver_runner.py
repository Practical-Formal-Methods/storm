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

import subprocess
import os
from termcolor import colored



def solver_runner(solver_path, smt_file, temp_core_folder, timeout, incremental, solver):

    temp_file_name = smt_file.replace(temp_core_folder, "")
    temp_file_name = temp_file_name.replace(".smt2", "")
    temp_file_name += "_output.txt"
    temp_file_path = temp_core_folder +  temp_file_name

    if solver in ["yices", "cvc4", "boolector"] and incremental == "yes":
        command = "timeout " + str(timeout) + "s " + solver_path + " --incremental " + smt_file + " > " + temp_file_path
    else:
        command = "timeout " + str(timeout) + "s " + solver_path + " " + smt_file + " > " + temp_file_path

    #print(colored(command, "yellow"))

    p = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE)
    terminal_output = p.stderr.read().decode()

    # Process terminal output first before result parsing
    if terminal_output.find("NULL pointer was dereferenced") != -1:
        return "nullpointer"
    if terminal_output.find("assert") != -1 or terminal_output.find("AssertionError") != -1:
        return "assertviolation"
    if terminal_output.find("segfault") != -1:
        return "segfault"
    if terminal_output.find("Fatal failure") != -1:
        return "fatalfailure"
    if terminal_output.find("Error") != -1:
        return "error"

    solver_output = read_result(temp_file_path, incremental)
    return solver_output




def read_result(file_path, incremental):
    try:
        with open(file_path, 'r') as f:
            lines = f.read().splitlines()
            #print(lines)
    except:
        print(colored("CANT OPEN THE FILE", "red", attrs=["bold"]))
        return "error"


    for line in lines:
        if line.find("Parse Error") != -1:
            os.remove(file_path)
            return "parseerror"

        if line.find("Segmentation fault") != -1:
            os.remove(file_path)
            return "segfault"

        # java.lang.NullPointerException
        if line.find("NullPointerException") != -1:
            os.remove(file_path)
            return "nullpointer"

        if line.find("ASSERTION VIOLATION") != -1:
            os.remove(file_path)
            return "assertviolation"

        # java.lang.AssertionError
        if line.find("AssertionError") != -1:
            os.remove(file_path)
            return "assertviolation"

        if line.find("CAUGHT SIGNAL 15") != -1:
            os.remove(file_path)
            return "timeout"


    # Uninteresting problems
    for line in lines:
        if line.find("error") != -1 or line.find("unsupported reserved word") != -1:
            os.remove(file_path)
            return "error"
        if line.find("failure") != -1:
            os.remove(file_path)
            return "error"
    if len(lines) == 0:
        os.remove(file_path)
        return "timeout"


    # Incremental mode
    if incremental == "yes":
        # If any result is unsat, return unsat
        for line in lines:
            if line.find("unsat") != -1:
                os.remove(file_path)
                return "unsat"

        for line in lines:
            if line.find("unknown") != -1:
                os.remove(file_path)
                return "unknown"

        os.remove(file_path)
        return "sat"



    if len(lines) > 0:
        if lines[0] == "sat" or lines[0] == "unsat" or lines[0] == "unknown":
            os.remove(file_path)
            return lines[0]
        else:
            return "error"
    else:
        os.remove(file_path)
        return "timeout"