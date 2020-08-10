bug_20_parameters = {
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
        "theory" : "QF_UFIDL",
        "buggy_mutant" : "mutant_932.smt2",
        "solver": "yices",
        "solverbin": "/home/numair/yices_versions/yices_140d/bin/yices-smt2",
        "fixed_solverbin": "/home/numair/yices_versions/yices_931f/bin/yices-smt2"
}


def get_bug20_parameters_dict():
    return bug_20_parameters

