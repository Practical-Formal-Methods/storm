## Bug ID 6

**Solver**: `z3 (https://github.com/Z3Prover/z3)`
<br>
**Buggy commit**: `da2f5cc36230b44e9043f099df7dabcb4f6647f7`
<br>
**Fixed commit**: `05da2508bfecfdf6fdfb5bcac821b19a753df01c`
<br>
**Issue**: `https://github.com/Z3Prover/z3/issues/2873`
<br>
**Logic**: `QF_BV`
<br>
**Mode**: `non-incremental`
<br>
**Seed file**: `QF_BV/app1/bench_1393.smt2`

### Storm command

```
storm --reproduce=bug6 --seed=1595625837
```



This will generate 1000 mutants of the seed file `seed.smt2` and copy the buggy mutant to this folder with the 
name `mutant_217.smt2`. 
The mutant has three levels in the assertion stack and is 
```
sat
``` 

But the buggy version of z3 returns: 
```
unsat
``` 
You can verify this by running this file with the buggy version of z3. 


