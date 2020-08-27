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

import time

class MainArgumentParser(object):

    def __init__(self):
        self.parsed_arguments = dict()
        self.verbose = 0
        self.core = None
        self.cores = None
        self.server = None
        self.seed = None
        self.ddebug = None
        self.benchmark = None
        self.theory = None
        self.solverbin = None
        self.solver = None
        self.reproduce = None
        self.min = None
        self.file_path = None
        self.check_sat_using = None
        self.incremental = None


    def parse_arguments(self, parser):
        parser.add_argument("--verbose", help="Verbose")
        parser.add_argument("--core", help="core to run on")
        parser.add_argument("--cores", help="number of cores to run on")
        parser.add_argument("--server", help="server")
        parser.add_argument("--seed", help="seed for randomness")
        parser.add_argument("--ddebug", help="Delta Debugger")
        parser.add_argument("--benchmark", help="Path to benchmark folder")
        parser.add_argument("--theory", help="Theory")
        parser.add_argument("--solverbin", help="path to solver bin")
        parser.add_argument("--solver", help="solver name e.g. z3, cvc4")
        parser.add_argument("--reproduce", help="reproduce bugs reported in our FSE 2020 paper")
        parser.add_argument("--min", nargs='?', const=True, default=False, help="Minimization mode")
        parser.add_argument("--file_path", help="path to a SMT file")
        parser.add_argument("--check_sat_using", help="check_sat_using (only for minimizer)")
        parser.add_argument("--incremental", nargs='?', const=True, default=False, help="incremental")


        arguments = vars(parser.parse_args())

        SEED = arguments["seed"]
        if SEED is None:
            SEED = str(int(time.time()))
            print("####### [NO SEED PROVIDED] - Using Unix time as seed: ", end="")
            print(SEED)
        else:
            print("####### Provided Seed: " + str(SEED))

        self.verbose = arguments["verbose"] if arguments["verbose"] is not None else 0
        self.core = arguments["core"] if arguments["core"] is not None else "0"
        self.cores = arguments["cores"] if arguments["cores"] is not None else None
        self.server = arguments["server"] if arguments["server"] is not None else "local"
        self.seed = SEED
        self.ddebug = True if arguments["ddebug"] is not None else False
        self.benchmark = arguments["benchmark"]
        self.theory = arguments["theory"]
        self.solverbin = arguments["solverbin"]
        self.solver = arguments["solver"]
        self.reproduce = arguments["reproduce"]
        self.min = arguments["min"]
        self.file_path = arguments["file_path"]
        self.check_sat_using = arguments["check_sat_using"]
        self.incremental = arguments["incremental"]


    def get_arguments(self):
        self.parsed_arguments["verbose"] = self.verbose
        self.parsed_arguments["core"] = self.core
        self.parsed_arguments["cores"] = self.cores
        self.parsed_arguments["server"] = self.server
        self.parsed_arguments["seed"] = self.seed
        self.parsed_arguments["ddebug"] = self.ddebug
        self.parsed_arguments["benchmark"] = self.benchmark
        self.parsed_arguments["theory"] = self.theory
        self.parsed_arguments["solverbin"] = self.solverbin
        self.parsed_arguments["solver"] = self.solver
        self.parsed_arguments["reproduce"] = self.reproduce
        self.parsed_arguments["min"] = self.min
        self.parsed_arguments["file_path"] = self.file_path
        self.parsed_arguments["check_sat_using"] = self.check_sat_using
        self.parsed_arguments["incremental"] = self.incremental
        return self.parsed_arguments
