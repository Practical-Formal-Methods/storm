### Bug ID 11

**Solver**: `z3str3 (https://github.com/Z3Prover/z3)`
<br>
**Buggy commit**: `41ab578593b5f3acf8d62b0fc3a3c7fa745ee67d`
<br>
**Fixed commit**: `9f6a733ff6a9be7668d0177be9be50d34444cc06`
<br>
**Issue**: `https://github.com/Z3Prover/z3/issues/3031`
<br>
**Logic**: `QF_S`
<br>
**Mode**: `incremental`
<br>
**Seed file**: `QF_S/amazon/z3-regex-1-graft-rotate-fuzz.smt2`


### Storm command

```
storm --reproduce=bug11 --seed=1595648319
```



This will generate 1000 mutants of the seed file `seed.smt2` and copy the buggy mutant to this folder with the 
name `mutant_11.smt2`. 
The mutant is 
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

But the buggy version of z3str3 returns: 
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
unsat
unsat
unsat
unsat
unsat
unsat
unsat
unsat
unsat
unsat
unsat
unsat
unsat
unsat
unsat
unsat
unsat
unsat
unsat
unsat
unsat
unsat

``` 
You can verify this by running this file with the buggy version of z3. 


