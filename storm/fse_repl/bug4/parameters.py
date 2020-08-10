bug_4_parameters = {
        "max_depth": 64,
        "max_assert": 64,
        "enrichment_steps": 1000,
        "number_of_mutants": 1000,
        "mutant_generation_timeout" : 900,
        "mutant_running_timeout" : 900,
        "solver_timeout" : 60,
        "check_sat_using" : ["no", "no"],
        "check_sat_using_options" : ["horn", "(then horn-simplify default)", "dom-simplify", "(then dom-simplify smt)"],
        "incremental": ["yes", "yes"],
        "theory" : "QF_UFLIA",
        "buggy_mutant" : "mutant_700.smt2",
        "solver" : "z3",
        "solverbin" : "/home/numair/z3_versions/z3_62ea/bin/z3",
        "fixed_solverbin" : "/home/numair/z3_versions/z3_321b/bin/z3"
}


def get_bug4_parameters_dict():
    return bug_4_parameters
