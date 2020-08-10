## Bug ID 4

**Solver**: `z3 (https://github.com/Z3Prover/z3)`
<br>
**Buggy commit**: `62ea86d5d211a18117ef24d59a6a19dbbb2de8f8`
<br>
**Fixed commit**: `321bad2c84c9bb0c58f44d5797bdf993b47b09d4`
<br>
**Issue**: `https://github.com/Z3Prover/z3/issues/2829`
<br>
**Logic**: `QF_UFLIA`
<br>
**Mode**: `incremental`

### Storm command

```
storm --reproduce=bug4 --seed=1595620813
```



This will generate 1000 mutants of the seed file `seed.smt2` and copy the buggy mutant to this folder with the 
name `mutant_700.smt2`. 
The mutant has eleven levels in the assertion stack and is 
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
unsat
sat
sat
``` 
You can verify this by running this file with the buggy version of z3. 


