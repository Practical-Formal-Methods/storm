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

from storm.runner.z3_python_api import check_satisfiability, convert_ast_to_expression, get_model
from z3 import *
from termcolor import colored
import copy

class smtObject(object):
    def __init__(self, file_path, path_to_mutant_folder):
        self.path_to_orig_smt_file = file_path
        self.path_to_mutant_folder = path_to_mutant_folder
        self.orig_satisfiability = None
        self.valid = True
        self.orig_ast = None
        self.true_nodes = list()
        self.false_nodes = list()
        self.all_nodes = list()
        self.dummy_ast = None
        self.true_constructed_nodes = list()
        self.false_constructed_nodes = list()
        self.total_number_of_assertions = 0


        try:
            self.orig_ast = parse_smt2_file(file_path)
            self.dummy_ast = parse_smt2_file(file_path)
            self.total_number_of_assertions = len(self.orig_ast)

        except:
            print(colored("Exception while parsing orig smt file", "red", "on_white"))
            self.valid = False
        self.negated_ast = None
        self.model = None



    def get_validity(self):
        return self.valid
    def get_orig_ast(self):
        return self.orig_ast
    def get_negated_ast(self):
        return self.negated_ast
    def get_dummy_ast(self):
        return self.dummy_ast
    def get_orig_satisfiability(self):
        return self.orig_satisfiability
    def append_true_node(self, node):
        self.true_nodes.append(node)
    def append_false_node(self, node):
        self.false_nodes.append(node)
    def append_true_constructed_node(self, node):
        self.true_constructed_nodes.append(node)
    def append_false_constructed_node(self, node):
        self.false_constructed_nodes.append(node)
    def append_to_all_nodes(self, node):
        self.all_nodes.append(node)
    def get_all_nodes(self):
        return self.all_nodes
    def get_true_nodes(self):
        return self.true_nodes
    def get_false_nodes(self):
        return self.false_nodes
    def get_true_constructed_nodes(self):
        return self.true_constructed_nodes
    def get_false_constructed_nodes(self):
        return self.false_constructed_nodes
    def get_total_number_of_assertions(self):
        return self.total_number_of_assertions


    def check_satisfiability(self, timeout):
        self.orig_satisfiability = check_satisfiability(self.orig_ast, timeout)
        # SAT
        if self.orig_satisfiability == "sat":
            print(colored(self.path_to_orig_smt_file, "blue", attrs=["bold"]) + ": " + colored(self.orig_satisfiability, "green", attrs=["bold"]))
        # UNSAT
        if self.orig_satisfiability == "unsat":
            print(colored(self.path_to_orig_smt_file, "blue", attrs=["bold"]) + ": " + colored(self.orig_satisfiability, "red", attrs=["bold"]), end="")
            self.negated_ast = Not(convert_ast_to_expression(self.orig_ast))
            if check_satisfiability(self.negated_ast, timeout) == "timeout":
                print(colored("   timeout on unsat -> sat file", "red"))
                self.valid = False
            else:
                print(colored("   successfully converted unsat -> sat", "green"))
        # TIMEOUT
        if self.orig_satisfiability == "timeout":
            print(colored(self.path_to_orig_smt_file, "blue", attrs=["bold"]) + ": " + colored(self.orig_satisfiability, "red", "on_white"))


    def get_model(self):
        if self.orig_satisfiability == "sat":
            self.model = get_model(self.orig_ast)
        if self.orig_satisfiability == "unsat":
            self.model = get_model(self.negated_ast)
        return self.model




