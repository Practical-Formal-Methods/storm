bug_2_parameters = {
        "max_depth": 20,
        "max_assert": 20,
        "enrichment_steps": 1000,
        "number_of_mutants": 1000,
        "mutant_generation_timeout" : 900,
        "mutant_running_timeout" : 900,
        "solver_timeout" : 60,
        "check_sat_using" : ["no", "no"],
        "check_sat_using_options" : ["horn", "(then horn-simplify default)", "dom-simplify", "(then dom-simplify smt)"],
        "incremental": ["yes", "yes"],
        "theory" : "QF_S",
        "buggy_mutant" : "mutant_407.smt2",
        "solver" : "z3",
        "solverbin" : "/home/numair/z3_versions/z3_5a68/bin/z3",
        "fixed_solverbin" : "/home/numair/z3_versions/z3_ce0c/bin/z3"
}


def get_bug2_parameters_dict():
    return bug_2_parameters

