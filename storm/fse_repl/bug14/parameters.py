bug_14_parameters = {
        "max_depth": 64,
        "max_assert": 64,
        "enrichment_steps": 1000,
        "number_of_mutants": 1000,
        "mutant_generation_timeout" : 900,
        "mutant_running_timeout" : 900,
        "solver_timeout" : 60,
        "check_sat_using" : ["no", "no"],
        "check_sat_using_options" : ["dom-simplify"],
        "incremental": ["yes", "yes"],
        "theory" : "QF_BV",
        "buggy_mutant" : "mutant_11.smt2",
        "solver": "yices",
        "solverbin": "/home/numair/yices_versions/yices_beb8/bin/yices-smt2 --mcsat",
        "fixed_solverbin": "/home/numair/yices_versions/yices_b5f1/bin/yices-smt2 --mcsat"
}


def get_bug14_parameters_dict():
    return bug_14_parameters
