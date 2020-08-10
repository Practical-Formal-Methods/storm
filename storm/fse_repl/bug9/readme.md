## Bug ID 9

**Solver**: `z3 (https://github.com/Z3Prover/z3)`
<br>
**Buggy commit**: `1aea0d2c8bb177ca9b2c9e04a2a13850f54e36dc`
<br>
**Fixed commit**: `7d8b56027fb6df40abf99851508adba9d360d6c6`
<br>
**Issue**: `https://github.com/Z3Prover/z3/issues/3068`
<br>
**Logic**: `UF`
<br>
**Mode**: `non-incremental`
<br>
**Seed file**: `UF/instantiated/dl_remove_postcondition_of_dl_remove_16_4.smt2`


### Storm command

```
storm --reproduce=bug9 --solver=z3 --seed=1595636275
```



This will generate 1000 mutants of the seed file `seed.smt2` and copy the buggy mutant to this folder with the 
name `mutant_116.smt2`. 
The mutant is 
```
sat
``` 

But the buggy version of z3 returns: 
```
unsat
``` 
You can verify this by running this file with the buggy version of z3. 


