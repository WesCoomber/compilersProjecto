# compilersProjecto
Extending flake8 linting rules.  
Project by: Wesley Coomber, Rose Howell, Steven Sprecher, Kristen Escher

# flake8-Smart

A [flake8](https://flake8.readthedocs.io) linter plug-in that checks for bugs and bad practices which flake8 doesn't
handle by default. The flake8-Smart plugin focuses on security and optimization
for the target Python file.

## Installation
First, install the base flake8 linter tool:
```
$ python<version> -m pip install flake8
```

Then, install the new flake8-plugin called flake8-Smart.

```
$ cd /compilersProjecto/flake8-Smart/
$ python setup.py install .
```

## Usage

After installation, the `flake8-Smart` extension is active by default.  
Verify this by checking `flake8 --version` for the flake8-Smart extension.  
To lint a file, run `flake8 test.py` where `test.py` is the file you would like to lint.  

## New Linter Warnings

### Security and Safety

* `A370`: Insecure hash function usage
* `A371`: Insecure cipher block mode

### Redundancy and complexity

* `A421`: Dead code after `if()` constant number value
* `A422`: Dead code after conditional evaluating constant boolean value
* `A423`: Dead code after a conditional statement that is indirectly given a constant value
* `A200`: Redundant or superfluous constant assignment within a loop


## The structure of the directory

Base dir of the project is `/compilersProjecto/`  
Our plug-in is in `/compilersProjecto/flake8-Smart/flake8_Smart.py`  
Our results are in `/compilersProjecto/our_stuff.log`  
A PDF of our report is in `/compilersProjecto/linter.pdf`  

```
compilersProjecto
- flake8-Smart/
    - flake8_Smart.py
    - reinstall.sh
    - setup.py
    - tests/
        - A200.py
        - A370.py
        - A371.py
        - A421.py
        - A422.py
        - A423.py
- helloWorldTest.py
- linter.pdf
- python_repository/
    - logs/
        - eyeo_sorted.log
        - our_plugin_sorted.log
        - our_stuff.log
        - out_plugin.log
        - vanilla_f8.log
    - pull_files_we_triggered_on.bash
    - python_code/
        - [3516 Python files for testing]
    - remove_new_rules.py
- README.md
```

## Instructions on reproducing our results

Commands to generate our experiment results:
```
$ cd python_repository/python_code  # make sure you have flake8-eyeo + flake8-Smart plugin 
$ flake8 * > ../logs/our_stuff.log
$ cd ../
$ python2.7 remove_new_rules /logs/our_stuff.log /logs/our_plugin_sorted.log /logs/eyeo_sorted.log
$ ./pull_files_we_triggered_on.bash logs/our_plugin_sorted.log python_code FILES_WE_TRIGGERED_ON
$ ./gather_plugin_error_data.bash logs/our_plugin_sorted.log
```
