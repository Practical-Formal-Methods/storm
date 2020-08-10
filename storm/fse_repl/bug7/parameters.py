bug_7_parameters = {
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
        "theory" : "LIA",
        "buggy_mutant" : "mutant_104.smt2",
        "solver" : "z3",
        "solverbin" : "/home/numair/z3_versions/z3_00e4/bin/z3",
        "fixed_solverbin" : "/home/numair/z3_versions/z3_c9be/bin/z3"
}


def get_bug7_parameters_dict():
    return bug_7_parameters
