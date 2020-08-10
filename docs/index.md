---
layout: default
---

## Detecting Critical Bugs in SMT Solvers Using Blackbox Mutational Fuzzing

Formal methods use SMT solvers extensively for deciding formula
satisfiability, for instance, in software verification, 
systematic test generation, symbolic execution and program synthesis. However, 
due to their complex implementations, solvers may contain critical bugs that lead to 
unsound results. Given the wide applicability of solvers in software reliability, 
relying on such unsound results may have catastrophic consequences. STORM is
a novel blackbox mutational fuzzer for detecting critical bugs (also known as 
refutational soundness bugs) in SMT solvers.

## Soundness bugs detected so far:
STORM has detected many unique and previously unknown "refutational soundness" bugs in 
multiple mature SMT solvers. Here is a list of issues we filed on public bug tracking systems
for various SMT solvers.

[github.com/SRI-CSL/yices2/issues/150](https://github.com/SRI-CSL/yices2/issues/150) `[yices]` `[QF_UFIDL]` <br>
[github.com/SRI-CSL/yices2/issues/160](https://github.com/SRI-CSL/yices2/issues/160) `[yices]` `[QF_UFLRA]` <br>
[github.com/SRI-CSL/yices2/issues/167](https://github.com/SRI-CSL/yices2/issues/167) `[yices]` `[QF_UF]` <br>
[github.com/Z3Prover/z3/issues/2758](https://github.com/Z3Prover/z3/issues/2758) `[z3]` `[QF_S]` <br>
[github.com/Z3Prover/z3/issues/3067](https://github.com/Z3Prover/z3/issues/3067) `[z3str3]` `[QF_S]` <br>
[github.com/levnach/z3/issues/115](https://github.com/levnach/z3/issues/115) `[z3]` `[QF_NIA]` <br>
[github.com/levnach/z3/issues/116](https://github.com/levnach/z3/issues/116) `[z3]` `[QF_NRA]` <br>
[github.com/Z3Prover/z3/issues/2828](https://github.com/Z3Prover/z3/issues/2828) `[z3]` `[QF_S]` <br>
[github.com/Z3Prover/z3/issues/2871](https://github.com/Z3Prover/z3/issues/2871) `[z3]` `[QF_LIA]` <br>
[github.com/SRI-CSL/yices2/issues/170](https://github.com/SRI-CSL/yices2/issues/170) `[yices]` `[QF_NRA]` <br>
[github.com/Z3Prover/z3/issues/2829](https://github.com/Z3Prover/z3/issues/2829) `[z3]` `[QF_LIA]` <br>
[github.com/Z3Prover/z3/issues/2835](https://github.com/Z3Prover/z3/issues/2835) `[z3]` `[QF_UFLIA]` <br>
[github.com/Z3Prover/z3/issues/2873](https://github.com/Z3Prover/z3/issues/2873) `[z3]` `[QF_BV]` <br>
[github.com/Z3Prover/z3/issues/2993](https://github.com/Z3Prover/z3/issues/2993) `[z3]` `[QF_S]` <br>
[github.com/levnach/z3/issues/114](https://github.com/levnach/z3/issues/114) `[z3]` `[AUFNIRA]` <br>
[github.com/Z3Prover/z3/issues/3052](https://github.com/Z3Prover/z3/issues/3052) `[z3]` `[LIA]` <br>
[github.com/Z3Prover/z3/issues/3058](https://github.com/Z3Prover/z3/issues/3058) `[z3]` `[QF_BVFP]` <br>
[github.com/Z3Prover/z3/issues/3068](https://github.com/Z3Prover/z3/issues/3068) `[z3]` `[UF]` <br>
[github.com/SRI-CSL/yices2/issues/169](https://github.com/SRI-CSL/yices2/issues/169) `[yices]` `[QF_UFIDL]` <br>
[github.com/SRI-CSL/yices2/issues/170](https://github.com/SRI-CSL/yices2/issues/170) `[yices]` `[QF_NRA]` <br>
[github.com/Z3Prover/z3/issues/2994](https://github.com/Z3Prover/z3/issues/2994) `[z3str3]` `[QF_S]` <br>
[github.com/Z3Prover/z3/issues/3031](https://github.com/Z3Prover/z3/issues/3031) `[z3str3]` `[QF_S]` <br>
[github.com/Z3Prover/z3/issues/2916](https://github.com/Z3Prover/z3/issues/2916) `[z3]` `[QF_S]` <br>
[github.com/Z3Prover/z3/issues/2925](https://github.com/Z3Prover/z3/issues/2925) `[z3]` `[QF_FP]` <br>
[github.com/Z3Prover/z3/issues/3040](https://github.com/Z3Prover/z3/issues/3040) `[z3]` `[QF_BV]` <br>
[github.com/Z3Prover/z3/issues/3096](https://github.com/Z3Prover/z3/issues/3096) `[z3]` `[QF_NIA]` <br>
[github.com/Z3Prover/z3/issues/3256](https://github.com/Z3Prover/z3/issues/3256) `[z3]` `[AUFNIRA]` <br>
[github.com/Z3Prover/z3/issues/3822](https://github.com/Z3Prover/z3/issues/3822) `[z3]` `[BV]` <br>
[github.com/Z3Prover/z3/issues/3948](https://github.com/Z3Prover/z3/issues/3948) `[z3]` `[AUFDTLIA]` <br>
[github.com/Z3Prover/z3/issues/3949](https://github.com/Z3Prover/z3/issues/3949) `[z3]` `[QF_UFLRA]` <br>
[github.com/Z3Prover/z3/issues/4590](https://github.com/Z3Prover/z3/issues/4590) `[z3str3]` `[QF_S]` <br>
[github.com/SRI-CSL/yices2/issues/280](https://github.com/SRI-CSL/yices2/issues/280) `[yices]` `[QF_NRA]`   
