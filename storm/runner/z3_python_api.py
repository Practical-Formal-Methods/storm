"""
Copyright 2020 MPI-SWS

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import multiprocessing
from termcolor import colored
from z3 import *





def check_satisfiability(ast, timeout):
    """

    :param ast: z3 ast vector
    :param timeout: Integer
    :return: string
    """
    def check_sat(ast, output):
        sol = Solver()
        sol.add(ast)
        satis = sol.check()
        if satis == sat:
            output.value = "sat".encode()
        if satis == unsat:
            output.value = "unsat".encode()


    output = multiprocessing.Array('c', b'unknown')
    process = multiprocessing.Process(target=check_sat, args=(ast, output))
    process.start()
    process.join(timeout)
    if process.is_alive():
        process.terminate()
        return "timeout"
    else:
        satisfiability = output.value.decode()
        return satisfiability



def convert_ast_to_expression(ast):
    expression = ast[0]
    for i in range(1, len(ast)):
        expression = And(expression, ast[i])
    return expression


def get_model(ast):
    s = Solver()
    s.add(ast)
    satis = s.check()
    if satis != sat:
        print(colored("Why are you sending me an unsat ast ?", "red"))
        raise Exception
    model = s.model()
    return model