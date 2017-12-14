# compilersProjecto
Oh boy flake8 improvements

# flake8-Smart

A [flake8](https://flake8.readthedocs.io) extension that checks for some bad practices which flake8 doesn't
handle by default. The flake8-Smart plug-in focuses on security and optimization for the target python file.
//TODO NEED TO RENAME 'FLAKE8-EYEO' TO A NEW ORIGINAL NAME (FOR EXAMPLE FLAKE8-SMART) AND FIX THE INSTALLATION FILES FOR THE NEW NAMED PLUG-IN.

## Installation

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
* `A200`: Redundant or superfluos constant assignment within a loop

=======
TODO:

Commands to generate results:
cd python_repository/python_code
#make sure you have flake8-eyeo + plugin 
flake8 * > ../logs/our_stuff.log
cd ..
python2.7 remove_new_rules /logs/our_stuff.log /logs/our_plugin_sorted.log /logs/eyeo_sorted.log
./pull_files_we_triggered_on.bash logs/our_plugin_sorted.log python_code FILES_WE_TRIGGERED_ON
./gather_plugin_error_data.bash logs/our_plugin_sorted.log
