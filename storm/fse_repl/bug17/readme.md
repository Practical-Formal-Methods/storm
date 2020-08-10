### Bug ID 17

**Solver**: `z3 (https://github.com/Z3Prover/z3)`
<br>
**Buggy commit**: `a069b6566903968e5482057d6ac5d2a36d5fbf55`
<br>
**Fixed commit**: `506fbf96725f8cc5696354ce6d7f3179f40d101f`
<br>
**Issue**: `https://github.com/Z3Prover/z3/issues/2799`
<br>
**Logic**: `QF_S`
<br>
**Mode**: `non-incremental`
<br>
**Seed file**: `cmu-prereg-fmf.smt2`


### Storm command

```
storm --reproduce=bug17 --seed=1595783287
```


This will generate 1000 mutants of the seed file `seed.smt2` and copy the buggy mutant to this folder with the 
name `mutant_0.smt2`. 
The mutant is 
```
sat
``` 

But the buggy version of z3 returns: 
```
unsat
``` 
You can verify this by running this file with the buggy version of z3. 


