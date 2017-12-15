# compilersProjecto
Oh boy flake8 improvements

Project by: Wesley Coomber, Rose Howell, Steven Sprecher, Kristen Escher

# flake8-Smart

A [flake8](https://flake8.readthedocs.io) extension plug-in that checks for some bugs and bad practices which flake8 doesn't
handle by default. The flake8-Smart plug-in focuses on security and optimization for the target python file.

## Installation
First install base flake8 linter tool.
To install Flake8, open an interactive shell and run:

`python<version> -m pip install flake8`

Then install the new flake8-plugin called flake8-Smart.
Go to /codingtools/flake8-Smart directory. (For example `/Users/wcoomber/codingtools/flake8-Smart`)
Run `python setup.py install`.

## Usage

Just run `flake8` (you have to install it seperately) on your source files.
After installation the `flake8-Smart` extension is active by default.

## Warnings

### Security and Safety

* `A370`: Insecure hash function usage
* `A371`: Insecure cipher block modes

### Redundancy and complexity

* `A421`: Dead code after if() constant number value
* `A422`: Dead code after conditional evaluating constant boolean value
* `A423`: Dead code after a conditional statement that is indirectly given a constant value
* `A200`: Redundant or superfluous constant assignment within a loop

=======
Instructions on reproducing our results.

Commands to generate experiment results:
cd python_repository/python_code
#make sure you have flake8-eyeo + flake8-Smart plugin 
flake8 * > ../logs/our_stuff.log
cd ..
python2.7 remove_new_rules /logs/our_stuff.log /logs/our_plugin_sorted.log /logs/eyeo_sorted.log
./pull_files_we_triggered_on.bash logs/our_plugin_sorted.log python_code FILES_WE_TRIGGERED_ON
./gather_plugin_error_data.bash logs/our_plugin_sorted.log
