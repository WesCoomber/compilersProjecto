#!/bin/bash

if [ "$#" -ne 3 ]; then
    echo "Usage: ./pull_files_we_triggered_on.bash <log of just our error messages> <path to code repository> <file destination>"
    exit
fi

OUR_ERRORS=$1
PY_CODE=$2
DESTINATION=$3

FILES_TO_MOVE=$(cat $OUR_ERRORS | awk -F '/' '{print $2}' | awk -F ':' '{print $1}' | sort -u)

if [[ -d $DESTINATION ]]
then   
   continue 
else
    mkdir $DESTINATION
fi

for file in $FILES_TO_MOVE; do
    cp $PY_CODE/$file $DESTINATION/
done



