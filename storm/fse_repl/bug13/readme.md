### Bug ID 13

**Solver**: `cvc4 (https://github.com/CVC4/CVC4)`
<br>
**Buggy commit**: `008d6b51baec353f45324e1d9407d898866cf688`
<br>
**Fixed commit**: `2b4e146c3a090e21b64d48ebb4308e5ec58a8c4b`
<br>
**Issue**: `https://github.com/CVC4/CVC4/issues/3538`
<br>
**Logic**: `QF_LIA`
<br>
**Mode**: `incremental + --sygus-inference`
<br>
**Seed file**: `/QF_LIA/CAV_2009_benchmarks/smt/20-vars/problem__003.smt2`


### Storm command

```
storm --reproduce=bug13 --seed=1595772671
```



This will generate 1000 mutants of the seed file `seed.smt2` and copy the buggy mutant to this folder with the 
name `mutant_10.smt2`. 
The mutant is 
```
sat
sat
sat
``` 

But the buggy version of cvc4 returns: 
```
sat
sat
unsat
``` 
You can verify this by running this file with the buggy version of cvc4. 


