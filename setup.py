from setuptools import setup,find_packages
import os

# Setting home
storm_home = os.path.dirname(os.path.realpath(__file__))
config_file = os.path.join(storm_home, "storm", "config.py")
line = 'config={"home":"' + storm_home + '"}'
file = open(config_file, "w")
file.write(line)
file.close()

setup(
    name='storm',
    version='0.0.1',
    description='Fuzzing SMT solvers for soundness refutational soundness bugs',
    author='Numair Mansur',
    author_email='numair@mpi-sws.org',
    url='https://practical-formal-methods.github.io/storm/',
    keywords='fuzzing',
    packages=find_packages(),
    install_requires=['termcolor', 'z3-solver', 'configparser'],
    entry_points={
        'console_scripts': ['storm = storm.__main__:main']
    }
)