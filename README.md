# compilersProjecto
Oh boy flake8 improvements

helloWorldTest.py is the test file that I am running flake8 on with this command:
flake8 helloWorldTest.py

I get these warnings on the helloWorldTest.py file:


helloWorldTest.py:3:5: F841 local variable 'a' is assigned to but never used
helloWorldTest.py:7:11: A101 use lists for data that have order
helloWorldTest.py:15:3: A111 wesTEST redundant parenthesis for if statement
helloWorldTest.py:19:3: A111 wesTEST redundant parenthesis for if statement

TODO:
Warning for if(0) and if(False), everything inside that if statement is dead code
Warning for dead code after sys.exit




Commands to generate results:
cd python_repository/python_code
#make sure you have flake8-eyeo + plugin 
flake8 * > ../logs/our_stuff.log
cd ..
python2.7 remove_new_rules /logs/our_stuff.log /logs/our_plugin_sorted.log /logs/eyeo_sorted.log
./pull_files_we_triggered_on.bash logs/our_plugin_sorted.log python_code FILES_WE_TRIGGERED_ON
./gather_plugin_error_data.bash logs/our_plugin_sorted.log

