## Bug ID 20

**Solver**: `yices2 (https://github.com/SRI-CSL/yices2)`
<br>
**Buggy commit**: `140de53864173e595d8686d1a269b887ef298434`
<br>
**Fixed commit**: `931fb4cd554156c009ba8de308fd7d98af280514`
<br>
**Issue**: `https://github.com/SRI-CSL/yices2/issues/150`
<br>
**Theory**: `QF_UFIDL`
<br>
**Seed file**: `QF_UFIDL/RDS/sorted_list_insert_noalloc6.smt2`

### Storm command

```
storm --reproduce=bug20 --seed=1595468702
```

This will generate 1000 mutants of the seed file `seed.smt2` and copy the buggy mutant to this folder with the name `mutant_932.smt2`. 
Both the seed file and the mutant is `sat` but the buggy version of yices return `unsat` on the mutant. 
You can verify this by running this file with the buggy version of yices. 
