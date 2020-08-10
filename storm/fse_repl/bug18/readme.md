### Bug ID 18

**Solver**: `z3 (https://github.com/Z3Prover/z3)`
<br>
**Buggy commit**: `28cb13fb96c15714eb244bf05d1d7f56e84cda5e`
<br>
**Fixed commit**: `7f61d084963a2a661c8e34a73e280e53593d507d`
<br>
**Issue**: `https://github.com/Z3Prover/z3/issues/2777`
<br>
**Logic**: `LIA`
<br>
**Mode**: `incremental + smt.arith.solver=1`
<br>
**Seed file**: `LIA/nested9_true-unreach-call.i_1887.smt2`


### Storm command

```
storm --reproduce=bug18 --seed=1595779325
```


This will generate 1000 mutants of the seed file `seed.smt2` and copy the buggy mutant to this folder with the 
name `mutant_102.smt2`. 
The mutant is 
```
sat
sat
``` 

But the buggy version of z3 returns: 
```
unknown
unsat
``` 
You can verify this by running this file with the buggy version of z3. 


