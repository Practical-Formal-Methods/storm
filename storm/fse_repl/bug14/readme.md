### Bug ID 14

**Solver**: `yices (https://github.com/SRI-CSL/yices2)`
<br>
**Buggy commit**: `beb86582a159340dc70003fe5fa5edeb322e2b83`
<br>
**Fixed commit**: `b5f1d0a72e9e5568938549f830e3b5be2525f053`
<br>
**Issue**: `https://github.com/SRI-CSL/yices2/issues/164`
<br>
**Logic**: `QF_BV`
<br>
**Mode**: `incremental + --mcsat`
<br>
**Seed file**: `QF_BV/bench_ab/a637test0068.smt2`


### Storm command

```
storm --reproduce=bug14 --seed=1595773093
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

``` 

But the buggy version of yices returns: 
```
sat
sat
unsat
unsat
unsat
``` 
You can verify this by running this file with the buggy version of yices. 


