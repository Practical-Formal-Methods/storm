### Bug ID 19

**Solver**: `z3str3 (https://github.com/Z3Prover/z3)`
<br>
**Buggy commit**: `d6df51951f4cdc95f0dfd3b1297d04a465d8f2ca`
<br>
**Fixed commit**: `7f61d084963a2a661c8e34a73e280e53593d507d`
<br>
**Issue**: `https://github.com/Z3Prover/z3/issues/2301`
<br>
**Logic**: `QF_S`
<br>
**Mode**: `non-incremental + smt.string_solver=z3str3`
<br>
**Seed file**: `QF_S/concats-extracts-small/concats-extracts-small-00024-0.smt25`


### Storm command

```
storm --reproduce=bug19 --seed=1595782865
```


This will generate 1000 mutants of the seed file `seed.smt2` and copy the buggy mutant to this folder with the 
name `mutant_105.smt2`. 
The mutant is 
```
sat
``` 

But the buggy version of z3 returns: 
```
unsat
``` 
You can verify this by running this file with the buggy version of z3. 


