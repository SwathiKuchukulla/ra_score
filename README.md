# ra_score


https://python-packaging.readthedocs.io/en/latest/minimal.html


### Changes

- Added MANIFEST.in: https://python-packaging.readthedocs.io/en/latest/non-code-files.html#adding-non-code-files
- Remove requirements.txt: use `install_requires` in setup.py instead. 
- Updated import path: 
	- import medicaid_model => from rascore import medicaid_model
	- from scroing import (conditionHierarchy) => from rascore.scoring import (conditionHierarchy)
	- from scoring import referenceFilesData => from rascore.scoring import referenceFilesData
- Created package `rascore`:
	- `ra_score` is github repository name
	- `rascore` is python package


### Test


```sh
# install rascore package
ra_score$ pip install .
Processing /Users/peter/Projects/evolent/ra_score
Building wheels for collected packages: Risk-Adjustment-Scoring-Engine
  Building wheel for Risk-Adjustment-Scoring-Engine (setup.py) ... done
  Stored in directory: /private/var/folders/tf/8vp5ftmd6w10xgpy7z3l6vs80000gn/T/pip-ephem-wheel-cache-jaqv6ksg/wheels/8f/60/29/572789d1a5f7a18a60d45bca0aa05ccffee357e32718fdc52e
Successfully built Risk-Adjustment-Scoring-Engine
Installing collected packages: Risk-Adjustment-Scoring-Engine
Successfully installed Risk-Adjustment-Scoring-Engine-0.1 

# open pytohn
$ python
Python 3.7.1 (default, Nov  6 2018, 18:46:03)
[Clang 10.0.0 (clang-1000.11.45.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> from rascore import medicaid_engine
>>>
```