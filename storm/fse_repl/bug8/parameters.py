bug_8_parameters = {
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
        "theory" : "QF_BVFP",
        "buggy_mutant" : "mutant_126.smt2",
        "solver" : "z3",
        "solverbin" : "/home/numair/z3_versions/z3_c9be/bin/z3",
        "fixed_solverbin" : "/home/numair/z3_versions/z3_55df/bin/z3"
}


def get_bug8_parameters_dict():
    return bug_8_parameters
