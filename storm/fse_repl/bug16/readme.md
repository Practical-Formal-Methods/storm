### Bug ID 16

**Solver**: `z3 (https://github.com/Z3Prover/z3)`
<br>
**Buggy commit**: `a05dec99cf1b86f40606dd38c3182dab454bd5cc`
<br>
**Fixed commit**: `506fbf96725f8cc5696354ce6d7f3179f40d101f`
<br>
**Issue**: `https://github.com/Z3Prover/z3/issues/2933`
<br>
**Logic**: `QF_BV`
<br>
**Mode**: `non-incremental`
<br>
**Seed file**: `QF_BV/bruttomesso/lfsr/lfsr_004_015_016.smt2`


### Storm command

```
storm --reproduce=bug16 --solver=z3 --seed=1595789292
```


This will generate 1000 mutants of the seed file `seed.smt2` and copy the buggy mutant to this folder with the 
name `mutant_121.smt2`. 
The mutant is 
```
sat
``` 

But the buggy version of z3 returns: 
```
unsat
``` 
You can verify this by running this file with the buggy version of z3. 


