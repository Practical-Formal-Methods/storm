bug_9_parameters = {
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
        "theory" : "UF",
        "buggy_mutant" : "mutant_116.smt2",
        "solver" : "z3",
        "solverbin" : "/home/numair/z3_versions/z3_1aea/bin/z3",
        "fixed_solverbin" : "/home/numair/z3_versions/z3_7d8b/bin/z3"
}


def get_bug9_parameters_dict():
    return bug_9_parameters
