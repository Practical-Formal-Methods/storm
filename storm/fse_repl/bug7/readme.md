## Bug ID 7

**Solver**: `z3 (https://github.com/Z3Prover/z3)`
<br>
**Buggy commit**: `00e43b6b88d6a1a111df7ebd762d11ba42eab4ab`
<br>
**Fixed commit**: `c9be09b18cd6a31eed49794b39a3722306e3fe7c`
<br>
**Issue**: `https://github.com/Z3Prover/z3/issues/3052`
<br>
**Logic**: `LIA`
<br>
**Mode**: `non-incremental`
<br>
**Seed file**: `LIA/psyco/099.smt2`

### Storm command

```
storm --reproduce=bug7 --solver=z3 --seed=1595635131
```



This will generate 1000 mutants of the seed file `seed.smt2` and copy the buggy mutant to this folder with the 
name `mutant_104.smt2`. The file is
```
sat
``` 

But the buggy version of z3 returns: 
```
unsat
``` 
You can verify this by running this file with the buggy version of z3. 


