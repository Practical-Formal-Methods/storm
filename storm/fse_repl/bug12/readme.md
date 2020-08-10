### Bug ID 12

**Solver**: `z3 (https://github.com/Z3Prover/z3)`
<br>
**Buggy commit**: `f810f25d8d612b00e2282e80bac7f909d0de3809`
<br>
**Fixed commit**: `1ac365ca7429421b4318576d18ccd6a8c5aaa20a`
<br>
**Issue**: `https://github.com/Z3Prover/z3/issues/3040`
<br>
**Logic**: `QF_BV`
<br>
**Mode**: `non-incremental`
<br>
**Seed file**: `QF_BV/sage/app7/bench_7183.smt2`


### Storm command

```
storm --reproduce=bug12 --solver=z3 --seed=1596100721
```



This will generate 1000 mutants of the seed file `seed.smt2` and copy the buggy mutant to this folder with the 
name `mutant_138.smt2`. 
The mutant is 
```
sat
``` 

But the buggy version of z3str3 returns: 
```
unsat
``` 
You can verify this by running this file with the buggy version of z3. 


