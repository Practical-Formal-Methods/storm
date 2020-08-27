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

from z3 import *
from storm.fuzzer.helper_functions import get_tree_depth

def get_max_depth(file_path):
    max_depth = 0
    ast = parse_smt2_file(file_path)
    for assertion in ast:
        assertion_depth = get_tree_depth(assertion, 64, optimization=False)
        if assertion_depth > max_depth:
            max_depth = assertion_depth
    return max_depth

def count_asserts(file_path):
    number_of_assertions = 0
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
    for line in lines:
        if line.find("(assert") != -1:
            number_of_assertions += 1
    return number_of_assertions

def count_lines(file_path):
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
    return len(lines)