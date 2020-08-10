bug_19_parameters = {
        "max_depth": 64,
        "max_assert": 64,
        "enrichment_steps": 1000,
        "number_of_mutants": 1000,
        "mutant_generation_timeout" : 900,
        "mutant_running_timeout" : 900,
        "solver_timeout" : 60,
        "check_sat_using" : ["no", "no"],
        "check_sat_using_options" : ["dom-simplify"],
        "incremental": ["no", "no"],
        "theory" : "QF_S",
        "buggy_mutant" : "mutant_105.smt2",
        "solver": "z3str3",
        "solverbin": "/home/numair/z3_versions/z3_d6df/bin/z3 smt.string_solver=z3str3",
        "fixed_solverbin": "/home/numair/z3_versions/z3_7f61/bin/z3 smt.string_solver=z3str3"
}


def get_bug19_parameters_dict():
    return bug_19_parameters
