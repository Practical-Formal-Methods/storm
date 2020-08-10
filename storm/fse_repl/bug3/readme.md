## Bug ID 3

**Solver**: `z3 (https://github.com/Z3Prover/z3)`
<br>
**Buggy commit**: `321bad2c84c9bb0c58f44d5797bdf993b47b09d4`
<br>
**Fixed commit**: `ad965ac89663016d6842a89fbab1583605d2ddf7`
<br>
**Issue**: `https://github.com/Z3Prover/z3/issues/2871`
<br>
**Logic**: `QF_LIA`
<br>
**Mode**: `incremental`
<br>
**Seed file**: `QF_LIA/check/bignum_lia1.smt2`

### Storm command

```
storm --reproduce=bug3 --seed=1595609033
```

This will generate 1000 mutants of the seed file `seed.smt2` and copy the buggy mutant to this folder with the 
name `mutant_11.smt2`. 
The mutant has five levels in the assertion stack and is 
```
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
unsat
sat
sat
``` 
You can verify this by running this file with the buggy version of z3. 