## Bug ID 1

**Solver**: `yices2 (https://github.com/SRI-CSL/yices2)`
<br>
**Buggy commit**: `1526d93178a9b39a85d9933eed14e3af76402cb7`
<br>
**Fixed commit**: `b5f1d0a72e9e5568938549f830e3b5be2525f053`
<br>
**Issue**: `https://github.com/SRI-CSL/yices2/issues/167`
<br>
**Theory**: `QF_UF`
<br>
**Mode**: `non-incremental`
<br>
**Seed file**: `QF_UF/QG-classification/loops6/gensys_brn029.smt2`


### Storm command
 
```
storm --reproduce=bug1 --seed=1595526152
```

This will generate 1000 mutants of the seed file `seed.smt2` and copy the buggy mutant to this folder with the 
name `mutant_472.smt2`. 
Both the seed file and the mutant is `sat` but the buggy version of yices returns `unsat` on the mutant. 
You can verify this by running this file with the buggy version of yices. 
