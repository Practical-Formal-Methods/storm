bug_1_parameters = {
        "max_depth": 64,
        "max_assert": 64,
        "enrichment_steps": 1000,
        "number_of_mutants": 1000,
        "mutant_generation_timeout" : 900,
        "mutant_running_timeout" : 900,
        "solver_timeout" : 60,
        "check_sat_using" : ["yes", "no"],
        "check_sat_using_options" : ["horn", "(then horn-simplify default)", "dom-simplify", "(then dom-simplify smt)"],
        "incremental": ["no", "no"],
        "theory" : "QF_UF",
        "buggy_mutant" : "mutant_472.smt2",
        "solver" : "yices",
        "solverbin" : "/home/numair/yices_versions/yices_1526/bin/yices-smt2",
        "fixed_solverbin" : "/home/numair/yices_versions/yices_b5f1/bin/yices-smt2"
}


def get_bug1_parameters_dict():
    return bug_1_parameters

