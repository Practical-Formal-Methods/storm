bug_12_parameters = {
        "max_depth": 64,
        "max_assert": 64,
        "enrichment_steps": 1000,
        "number_of_mutants": 1000,
        "mutant_generation_timeout" : 900,
        "mutant_running_timeout" : 900,
        "solver_timeout" : 60,
        "check_sat_using" : ["yes", "yes"],
        "check_sat_using_options" : ["dom-simplify"],
        "incremental": ["no", "no"],
        "theory" : "QF_BV",
        "buggy_mutant" : "mutant_138.smt2",
        "solver": "z3",
        "solverbin": "/home/numair/z3_versions/z3_f810/bin/z3",
        "fixed_solverbin": "/home/numair/z3_versions/z3_1ac3/bin/z3"
}


def get_bug12_parameters_dict():
    return bug_12_parameters
