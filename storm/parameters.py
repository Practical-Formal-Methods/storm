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

from termcolor import colored
from storm.fse_repl.bug1.parameters import get_bug1_parameters_dict
from storm.fse_repl.bug2.parameters import get_bug2_parameters_dict
from storm.fse_repl.bug3.parameters import get_bug3_parameters_dict
from storm.fse_repl.bug4.parameters import get_bug4_parameters_dict
from storm.fse_repl.bug5.parameters import get_bug5_parameters_dict
from storm.fse_repl.bug6.parameters import get_bug6_parameters_dict
from storm.fse_repl.bug7.parameters import get_bug7_parameters_dict
from storm.fse_repl.bug8.parameters import get_bug8_parameters_dict
from storm.fse_repl.bug9.parameters import get_bug9_parameters_dict
from storm.fse_repl.bug10.parameters import get_bug10_parameters_dict
from storm.fse_repl.bug11.parameters import get_bug11_parameters_dict
from storm.fse_repl.bug12.parameters import get_bug12_parameters_dict
from storm.fse_repl.bug13.parameters import get_bug13_parameters_dict
from storm.fse_repl.bug14.parameters import get_bug14_parameters_dict
from storm.fse_repl.bug15.parameters import get_bug15_parameters_dict
from storm.fse_repl.bug16.parameters import get_bug16_parameters_dict
from storm.fse_repl.bug17.parameters import get_bug17_parameters_dict
from storm.fse_repl.bug18.parameters import get_bug18_parameters_dict
from storm.fse_repl.bug19.parameters import get_bug19_parameters_dict
from storm.fse_repl.bug20.parameters import get_bug20_parameters_dict


def get_supported_theories(solver):
    theories =  {
                    "z3" : ["ALIA", "AUFNIA", "LRA", "QF_ALIA", "QF_AUFNIA", "QF_LRA", "QF_RDL", "QF_UFIDL",
                   "QF_UFNRA", "UFDTLIA", "AUFDTLIA", "AUFNIRA", "NIA", "QF_ANIA", "QF_AX", "QF_FP", "QF_NIA",
                    "QF_UFLIA", "UFLIA", "AUFLIA", "BV", "NRA", "QF_AUFBV", "QF_BV", "QF_IDL", "QF_NIRA",
                   "QF_UF", "QF_UFLRA", "UF", "UFLRA", "AUFLIRA", "LIA", "QF_ABV", "QF_AUFLIA", "QF_BVFP",
                   "QF_LIA", "QF_NRA", "QF_UFBV", "QF_UFNIA", "UFDT", "UFNIA", "QF_S"],

                "yices": ["QF_ABV", "QF_ALIA", "QF_AUFBV", "QF_AUFLIA", "QF_AX", "QF_BV", "QF_IDL", "QF_LIA", "QF_LIRA",
                  "QF_LRA", "QF_NIA", "QF_NIRA", "QF_NRA", "QF_RDL", "QF_UF", "QF_UFBV", "QF_UFIDL", "QF_UFLIA",
                  "QF_UFLRA", "QF_UFNIA", "QF_UFNIRA", "QF_UFNRA", "LRA",
                  "UFLRA"],

                "z3str3" : ["QF_S"],

                "smtinterpol" : ["QF_ABV", "QF_ALIA", "QF_AUFBV", "QF_AUFLIA", "QF_AX", "QF_BV", "QF_IDL", "QF_LIA", "QF_LIRA",
                  "QF_LRA", "QF_NIA", "QF_NIRA", "QF_NRA", "QF_RDL", "QF_UF", "QF_UFBV", "QF_UFIDL", "QF_UFLIA",
                  "QF_UFLRA", "QF_UFNIA", "QF_UFNIRA", "QF_UFNRA", "LRA",
                  "UFLRA"],

                "cvc4": ["ALIA", "AUFNIA", "LRA", "QF_ALIA", "QF_AUFNIA", "QF_LRA", "QF_RDL", "QF_UFIDL",
                   "QF_UFNRA", "UFDTLIA", "AUFDTLIA", "AUFNIRA", "NIA", "QF_ANIA", "QF_AX", "QF_FP", "QF_NIA",
                    "QF_UFLIA", "UFLIA", "AUFLIA", "BV", "NRA", "QF_AUFBV", "QF_BV", "QF_IDL", "QF_NIRA",
                   "QF_UF", "QF_UFLRA", "UF", "UFLRA", "AUFLIRA", "LIA", "QF_ABV", "QF_AUFLIA", "QF_BVFP",
                   "QF_LIA", "QF_NRA", "QF_UFBV", "QF_UFNIA", "UFDT", "UFNIA", "QF_S"],

                "mathsat" : ["QF_ABV", "QF_ABVFP", "QF_ABVFPLRA", "QF_ALIA", "QF_ANIA", "QF_AUFBV", "QF_AUFLIA",
                             "QF_AUFNIA", "QF_AX", "QF_BV", "QF_BVFP", "QF_BVFPLRA", "QF_FP", "QF_FPLRA", "QF_IDL",
                             "QF_LIA", "QF_LIRA", "QF_LRA", "QF_NIA", "QF_NIRA", "QF_NRA", "QF_RDL", "QF_UF", "QF_UFBV",
                             "QF_UFFP", "QF_UFIDL", "QF_UFLIA", "QF_UFLRA", "QF_UFNIA", "QF_UFNRA"],

                "bitwuzla" : ["BV", "QF_ABV", "QF_ABVFP", "QF_AUFBV", "QF_BV", "QF_BVFP", "QF_FP", "QF_UFBV", "QF_UFFP"]

    }
    return theories[solver]


parameters = {
        "max_depth": 20,
        "max_assert": 20,
        "enrichment_steps": 1000,
        "number_of_mutants": 1000,
        "mutant_generation_timeout" : 900, # 15 mins
        "mutant_running_timeout" : 900, # 15 mins
        "solver_timeout" : 120,
        "check_sat_using" : ["yes", "no"],  # remove an option if you want a single mode. Otherwise storm will choose with a prob
        "check_sat_using_options" : ["horn", "(then horn-simplify default)", "dom-simplify", "(then dom-simplify smt)"],
        "incremental": ["yes", "no"]    # remove an option if you want a single mode. Otherwise storm will choose with a prob
    }




def get_parameters_dict(replication_mode, bug_number):
    if not replication_mode:
        print("#######" + colored(" Getting the normal fuzzing parameters", "magenta", attrs=["bold"]))
        print(str(parameters))
        return parameters
    else:
        if bug_number == "bug1":
            print("#######" + colored(" Getting fuzzing parameters for BUG1", "yellow", attrs=["bold"]))
            return get_bug1_parameters_dict()
        elif bug_number == "bug2":
            print("#######" + colored(" Getting fuzzing parameters for BUG2", "yellow", attrs=["bold"]))
            return get_bug2_parameters_dict()
        elif bug_number == "bug3":
            print("#######" + colored(" Getting fuzzing parameters for BUG3", "yellow", attrs=["bold"]))
            return get_bug3_parameters_dict()
        elif bug_number == "bug4":
            print("#######" + colored(" Getting fuzzing parameters for BUG4", "yellow", attrs=["bold"]))
            return get_bug4_parameters_dict()
        elif bug_number == "bug5":
            print("#######" + colored(" Getting fuzzing parameters for BUG 5", "yellow", attrs=["bold"]))
            return get_bug5_parameters_dict()
        elif bug_number == "bug6":
            print("#######" + colored(" Getting fuzzing parameters for BUG 6", "yellow", attrs=["bold"]))
            return get_bug6_parameters_dict()
        elif bug_number == "bug7":
            print("#######" + colored(" Getting fuzzing parameters for BUG 7", "yellow", attrs=["bold"]))
            return get_bug7_parameters_dict()
        elif bug_number == "bug8":
            print("#######" + colored(" Getting fuzzing parameters for BUG 8", "yellow", attrs=["bold"]))
            return get_bug8_parameters_dict()
        elif bug_number == "bug9":
            print("#######" + colored(" Getting fuzzing parameters for BUG 9", "yellow", attrs=["bold"]))
            return get_bug9_parameters_dict()
        elif bug_number == "bug10":
            print("#######" + colored(" Getting fuzzing parameters for BUG 10", "yellow", attrs=["bold"]))
            return get_bug10_parameters_dict()
        elif bug_number == "bug11":
            print("#######" + colored(" Getting fuzzing parameters for BUG 11", "yellow", attrs=["bold"]))
            return get_bug11_parameters_dict()
        elif bug_number == "bug12":
            print("#######" + colored(" Getting fuzzing parameters for BUG 12", "yellow", attrs=["bold"]))
            return get_bug12_parameters_dict()
        elif bug_number == "bug13":
            print("#######" + colored(" Getting fuzzing parameters for BUG 13", "yellow", attrs=["bold"]))
            return get_bug13_parameters_dict()
        elif bug_number == "bug14":
            print("#######" + colored(" Getting fuzzing parameters for BUG 14", "yellow", attrs=["bold"]))
            return get_bug14_parameters_dict()
        elif bug_number == "bug15":
            print("#######" + colored(" Getting fuzzing parameters for BUG 15", "yellow", attrs=["bold"]))
            return get_bug15_parameters_dict()
        elif bug_number == "bug16":
            print("#######" + colored(" Getting fuzzing parameters for BUG 16", "yellow", attrs=["bold"]))
            return get_bug16_parameters_dict()
        elif bug_number == "bug17":
            print("#######" + colored(" Getting fuzzing parameters for BUG 17", "yellow", attrs=["bold"]))
            return get_bug17_parameters_dict()
        elif bug_number == "bug18":
            print("#######" + colored(" Getting fuzzing parameters for BUG 18", "yellow", attrs=["bold"]))
            return get_bug18_parameters_dict()
        elif bug_number == "bug19":
            print("#######" + colored(" Getting fuzzing parameters for BUG 19", "yellow", attrs=["bold"]))
            return get_bug19_parameters_dict()
        elif bug_number == "bug20":
            print("#######" + colored(" Getting fuzzing parameters for BUG20", "yellow", attrs=["bold"]))
            return get_bug20_parameters_dict()
        else:
            print("Please enter a valid bug number")

