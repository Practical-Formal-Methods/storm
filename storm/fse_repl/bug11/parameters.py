bug_11_parameters = {
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
        "theory" : "QF_S",
        "buggy_mutant" : "mutant_11.smt2",
        "solver": "z3str3",
        "solverbin": "/home/numair/z3_versions/z3_41ab/bin/z3 smt.string_solver=z3str3",
        "fixed_solverbin": "/home/numair/z3_versions/z3_9f6a/bin/z3 smt.string_solver=z3str3"
}


def get_bug11_parameters_dict():
    return bug_11_parameters
