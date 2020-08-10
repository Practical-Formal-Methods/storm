## Bug ID 10

**Solver**: `z3str3 (https://github.com/Z3Prover/z3)`
<br>
**Buggy commit**: `0146259ea402a8bf3996f1ca0d2d37ed69fddd35`
<br>
**Fixed commit**: `85fd139c7f7cb363fc35793e55acbd4465b58853`
<br>
**Issue**: `https://github.com/Z3Prover/z3/issues/2994`
<br>
**Logic**: `QF_S`
<br>
**Mode**: `non-incremental`
<br>
**Seed file**: `QF_S/sanitizer/ipv4-address2-translate-reverse-translate.smt2`


### Storm command

```
storm --reproduce=bug10 --seed=1596099711
```



This will generate 1000 mutants of the seed file `seed.smt2` and copy the buggy mutant to this folder with the 
name `mutant_184.smt2`. 
The mutant is 
```
sat
``` 

But the buggy version of z3str3 returns: 
```
unsat
``` 
You can verify this by running this file with the buggy version of z3str3. 


