bug_13_parameters = {
        "max_depth": 64,
        "max_assert": 64,
        "enrichment_steps": 1000,
        "number_of_mutants": 1000,
        "mutant_generation_timeout" : 900,
        "mutant_running_timeout" : 2000,
        "solver_timeout" : 120,
        "check_sat_using" : ["no", "no"],
        "check_sat_using_options" : ["dom-simplify"],
        "incremental": ["yes", "yes"],
        "theory" : "QF_LIA",
        "buggy_mutant" : "mutant_10.smt2",
        "solver": "cvc4",
        "solverbin": "/home/numair/cvc4_versions/cvc4_008d/bin/cvc4 --sygus-inference",
        "fixed_solverbin": "/home/numair/cvc4_versions/cvc4_2b4e/bin/cvc4 --sygus-inference"
}


def get_bug13_parameters_dict():
    return bug_13_parameters
