## Bug ID 5

**Solver**: `z3 (https://github.com/Z3Prover/z3)`
<br>
**Buggy commit**: `1fff7bb51da144635228ff114589efd50e3fcf92`
<br>
**Fixed commit**: `ce0ccc2e9ef9b5c71312a08795575cbd11c75c11`
<br>
**Issue**: `https://github.com/Z3Prover/z3/issues/2835`
<br>
**Logic**: `QF_UFLIA`
<br>
**Mode**: `incremental`
<br>
**Seed File** : `QF_UFLIA/Wisa/xs-05-17-1-5-1-5.smt2`

### Storm command

```
storm --reproduce=bug5 --seed=1595623605
```



This will generate 1000 mutants of the seed file `seed.smt2` and copy the buggy mutant to this folder with the 
name `mutant_405.smt2`. 
The mutant has 22 levels in the assertion stack and is 
```
sat
sat
sat
sat
sat
sat
sat
sat
sat
sat
sat
sat
sat
sat
sat
sat
sat
sat
sat
sat
sat
sat
``` 

But the buggy version of z3 returns: 
```
sat
sat
sat
sat
sat
sat
sat
sat
sat
sat
sat
unsat
sat
unsat
sat
unsat
unsat
unsat
unsat
unsat
unsat
unsat
``` 
You can verify this by running this file with the buggy version of z3. 


