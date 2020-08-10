bug_18_parameters = {
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
        "theory" : "LIA",
        "buggy_mutant" : "mutant_102.smt2",
        "solver": "z3",
        "solverbin": "/home/numair/z3_versions/z3_28cb/bin/z3 smt.arith.solver=1",
        "fixed_solverbin": "/home/numair/z3_versions/z3_7f61/bin/z3 smt.arith.solver=1"
}


def get_bug18_parameters_dict():
    return bug_18_parameters
