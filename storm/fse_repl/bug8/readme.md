## Bug ID 8

**Solver**: `z3 (https://github.com/Z3Prover/z3)`
<br>
**Buggy commit**: `c9be09b18cd6a31eed49794b39a3722306e3fe7c`
<br>
**Fixed commit**: `55df045f85645e38d54274f3591b09d60dd99146`
<br>
**Issue**: `https://github.com/Z3Prover/z3/issues/3058`
<br>
**Logic**: `QF_BVFP`
<br>
**Mode**: `non-incremental`
<br>
**Seed file**: `QF_BVFP/imperial_synthetic_fadd_to_exact_zero_klee_float.x86_64/query.18.smt2`

### Storm command

```
storm --reproduce=bug8 --solver=z3 --seed=1595635804
```



This will generate 1000 mutants of the seed file `seed.smt2` and copy the buggy mutant to this folder with the 
name `mutant_126.smt2`. 
The mutant is 
```
sat
``` 

But the buggy version of z3 returns: 
```
unsat
``` 
You can verify this by running this file with the buggy version of z3. 


