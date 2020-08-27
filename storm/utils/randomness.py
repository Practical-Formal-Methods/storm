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

import random
import string

class Randomness(object):
    def __init__(self, seed):
        self.seed = seed
        random.seed(self.seed)


    def get_random_integer(self, low, high):
        # high is inclusive
        return random.randint(low, high)

    def get_random_alpha_string(self, length):
        return "".join(random.choice(string.ascii_letters) for i in range(length))

    def get_random_alpha_numeric_string(self, length):
        return "".join(random.choice(string.ascii_letters + string.digits) for i in range(length))

    def get_seed(self):
        return self.seed

    def random_choice(self, list):
        return random.choice(list)

    def get_random_float(self, low, high):
        return str(self.get_random_integer(low,high)) + "." + str(self.get_random_integer(0,999))

    def shuffle_list(self, list):
        random.shuffle(list)

    def get_a_non_prime_integer(self, max):
        while True:
            number = self.get_random_integer(4, max)
            for i in range(2, number):
                if number % i == 0:
                    return number