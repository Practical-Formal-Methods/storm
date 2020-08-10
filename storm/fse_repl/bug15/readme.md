### Bug ID 15

**Solver**: `z3 (https://github.com/Z3Prover/z3)`
<br>
**Buggy commit**: `524434cfbb70eb25e96a8013e4548b347f20a16d`
<br>
**Fixed commit**: `feba0076966a7b9911699f7bed7a1138e049069e`
<br>
**Issue**: `https://github.com/Z3Prover/z3/issues/2965`
<br>
**Logic**: `QF_BV`
<br>
**Mode**: `non-incremental`
<br>
**Seed file**: `QF_BV/crafted/bitops2.smt2`


### Storm command

```
storm --reproduce=bug15 --solver=z3 --seed=1595773410
```


This will generate 1000 mutants of the seed file `seed.smt2` and copy the buggy mutant to this folder with the 
name `mutant_111.smt2`. 
The mutant is 
```
sat
``` 

But the buggy version of z3 returns: 
```
unsat
``` 
You can verify this by running this file with the buggy version of z3. 


