#!/bin/bash

OUTPUT="OUTPUT_vanilla_eyeo.log"
input_path="/Users/stevensprecher/Documents/Classes/Fall2017/583/project/compilersProjecto/python_repository/python_code"

for file in $(ls $input_path); do
    echo "flake8 $file"
    if flake8 $input_path/$file > $OUTPUT; then
        echo "success"
    else
        echo "failure" 
        echo $file > "$OUTPUT.error"
        
   fi 
    echo "done"
    echo ""
    echo ""
done
