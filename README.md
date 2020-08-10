![logo](https://user-images.githubusercontent.com/4897599/72667625-29075e00-3a1e-11ea-8179-776e9c4c938d.png)

![Python application](https://github.com/Practical-Formal-Methods/storm/workflows/Python%20application/badge.svg)
![Python package](https://github.com/Practical-Formal-Methods/storm/workflows/Python%20package/badge.svg)

## Installation:
```
git clone https://github.com/Practical-Formal-Methods/storm
virtualenv --python=/usr/bin/python3.7 venv
source venv/bin/activate
cd storm
python setup.py install
```

## Usage:

```
storm --benchmark=[PATH TO SEED FILES] --solverbin=[PATH TO SOLVER BIN] --solver=[SOLVER NAME]
```

To test the solver on a particular theory, use the `--theory` flag. For example:

```
storm --benchmark=[PATH TO SEED FILES] --solverbin=[PATH TO SOLVER BIN] --solver=[SOLVER NAME] --theory=LIA
```

To run `n` parallel instances of storm on `n` cores, use the `--cores` flag. For example:

```
storm --benchmark=[PATH TO SEED FILES] --solverbin=[PATH TO SOLVER BIN] --solver=[SOLVER NAME] --theory=LIA --cores=10
```

To obtain a smaller SMT instance that revealed a refutational soundness bug in an SMT solver, use:
```
storm --min --file_path=[PATH TO SMT INSTANCE] --solver=[SOLVER NAME] --solverbin=[PATH TO SOLVER BIN] --theory=[THEORY NAME] 
```
If the SMT instance is in incremental mode, use `--incremental` flag.


## Soundness bugs detected so far:
STORM has detected many unique and previously unknown "refutational soundness" bugs in 
multiple mature SMT solvers. Here is a list of issues we filed on public bug tracking systems
for various SMT solvers.

https://github.com/SRI-CSL/yices2/issues/150 `[yices]` `[QF_UFIDL]` <br>
https://github.com/SRI-CSL/yices2/issues/160 `[yices]` `[QF_UFLRA]` <br>
https://github.com/SRI-CSL/yices2/issues/167 `[yices]` `[QF_UF]` <br>
https://github.com/Z3Prover/z3/issues/2758 `[z3]` `[QF_S]` <br>
https://github.com/Z3Prover/z3/issues/3067 `[z3str3]` `[QF_S]` <br>
https://github.com/levnach/z3/issues/115 `[z3]` `[QF_NIA]` <br>
https://github.com/levnach/z3/issues/116 `[z3]` `[QF_NRA]` <br>
https://github.com/Z3Prover/z3/issues/2828 `[z3]` `[QF_S]` <br>
https://github.com/Z3Prover/z3/issues/2871 `[z3]` `[QF_LIA]` <br>
https://github.com/SRI-CSL/yices2/issues/170 `[yices]` `[QF_NRA]` <br>
https://github.com/Z3Prover/z3/issues/2829 `[z3]` `[QF_LIA]` <br>
https://github.com/Z3Prover/z3/issues/2835 `[z3]` `[QF_UFLIA]` <br>
https://github.com/Z3Prover/z3/issues/2873 `[z3]` `[QF_BV]` <br>
https://github.com/Z3Prover/z3/issues/2993 `[z3]` `[QF_S]` <br>
https://github.com/levnach/z3/issues/114 `[z3]` `[AUFNIRA]` <br>
https://github.com/Z3Prover/z3/issues/3052 `[z3]` `[LIA]` <br>
https://github.com/Z3Prover/z3/issues/3058 `[z3]` `[QF_BVFP]` <br>
https://github.com/Z3Prover/z3/issues/3068 `[z3]` `[UF]` <br>
https://github.com/SRI-CSL/yices2/issues/169 `[yices]` `[QF_UFIDL]` <br>
https://github.com/SRI-CSL/yices2/issues/170 `[yices]` `[QF_NRA]` <br>
https://github.com/Z3Prover/z3/issues/2994 `[z3str3]` `[QF_S]` <br>
https://github.com/Z3Prover/z3/issues/3031 `[z3str3]` `[QF_S]` <br>
https://github.com/Z3Prover/z3/issues/2916 `[z3]` `[QF_S]` <br>
https://github.com/Z3Prover/z3/issues/2925 `[z3]` `[QF_FP]` <br>
https://github.com/Z3Prover/z3/issues/3040 `[z3]` `[QF_BV]` <br>
https://github.com/Z3Prover/z3/issues/3096 `[z3]` `[QF_NIA]` <br>
https://github.com/Z3Prover/z3/issues/3256 `[z3]` `[AUFNIRA]` <br>
https://github.com/Z3Prover/z3/issues/3822 `[z3]` `[BV]` <br>
https://github.com/Z3Prover/z3/issues/3948 `[z3]` `[AUFDTLIA]` <br>
https://github.com/Z3Prover/z3/issues/3949 `[z3]` `[QF_UFLRA]` <br>
https://github.com/Z3Prover/z3/issues/4590 `[z3str3]` `[QF_S]` <br>
https://github.com/SRI-CSL/yices2/issues/280 `[yices]` `[QF_NRA]` 
 
## Reproducing bugs used in the evaluation section of our ESEC/FSE 2020 paper:
Please follow the instructions 
[here](https://github.com/Practical-Formal-Methods/storm/tree/master/storm/fse_repl).