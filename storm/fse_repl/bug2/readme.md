# Bug ID 2

### Some information about the bug

**Solver**: `z3-seq (https://github.com/Z3Prover/z3)`
<br>
**Buggy commit**: `5a68fc8c078c653c44b6227efe2720821f12026c`
<br>
**Fixed commit**: `ce0ccc2e9ef9b5c71312a08795575cbd11c75c11`
<br>
**Issue**: `https://github.com/Z3Prover/z3/issues/2828`
<br>
**Logic**: `QF_S`
<br>
**Seed file**: `lengths-concats/lengths-concats-00015-1.smt25`

### STORM command to reproduce the bug

```
storm --reproduce=bug2 --seed=1595605723
```

This will generate 1000 mutants of the seed file `seed.smt2` and copy the buggy mutant to this folder with the 
name `mutant_407.smt2`. 
The mutant has three levels in the assertion stack and is 
```
sat
sat
sat
``` 

But the buggy version of z3 returns: 
```
sat
unsat
unsat
``` 
You can verify this by running this file with the buggy version of z3. 
