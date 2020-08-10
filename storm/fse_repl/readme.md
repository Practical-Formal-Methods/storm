# Reproducing bugs used in the evaluation section of our ESEC/FSE 2020 paper:

Install STORM at version `b4961eff9a6392f668fa9aae5a94247735654dfa`. 
 
```
git clone https://github.com/Practical-Formal-Methods/storm
git checkout b4961eff9a6392f668fa9aae5a94247735654dfa
virtualenv --python=/usr/bin/python3.7 venv
source venv/bin/activate
cd storm
python setup.py install
```

To reproduce a bug, please follow the instructions within each bug ID folder. 
You can verify the bug by installing the specified version of the appropriate solver and running
the produced buggy SMT file.
