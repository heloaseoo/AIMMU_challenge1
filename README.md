# AIMMU_challenge1
AI Mons Meet-Up - Challenge #1

This is the code used to classify images on gender and age.

# BDD preparation
You must have the raw database (openu folder) in the same folder than your python files.
Example:
* face_sorter.py
* bdd_adjust.py
* openu/
## face_sorter.py
Just have to run the python file.
```
python face_sorter.py
```
## bdd_adjust.py
Just have to run the python file.
```
python bdd_adjust.py
```
### Parameters
The proportion of data for validation and test can be changed if needed:
```
VAL_PROP = 0.2
TEST_PROP = 0.1
```
(here we have 20% of the BDD used for validation and 10% for test)
