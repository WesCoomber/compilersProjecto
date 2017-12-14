#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: ./test.bash <log of just our error messages>"
    exit
fi

OUR_ERRORS=$1

lstA200=()
lstA370=()
lstA371=()
lstA421=()
lstA422=()
lstA423=()
lstA424=()

while read line; do
    CODE=$(echo $line | awk -F ':' '{print $4}' | awk -F ' ' '{print $1}')
    FILE=$(echo $line | awk -F '/' '{print $2}' | awk -F ':' '{print $1}')



    if [ $CODE = "A200" ]
    then
        lstA200+=($FILE)

    elif [ $CODE = "A370" ]
    then 
        lstA370+=($FILE)

    elif [ $CODE = "A371" ]
    then 
        lstA371+=($FILE)

    elif [ $CODE = "A421" ]
    then 
        lstA421+=($FILE)

    elif [ $CODE = "A422" ]
    then 
        lstA422+=($FILE)

    elif [ $CODE = "A423" ]
    then 
        lstA423+=($FILE)

    elif [ $CODE = "A424" ]
    then 
        lstA424+=($FILE)

    fi

done < <(cat $OUR_ERRORS)




sortA200=($(echo ${lstA200[@]} | tr " " "\n" | sort -u))
sortA370=($(echo ${lstA370[@]} | tr " " "\n" | sort -u))
sortA371=($(echo ${lstA371[@]} | tr " " "\n" | sort -u))
sortA421=($(echo ${lstA421[@]} | tr " " "\n" | sort -u))
sortA422=($(echo ${lstA422[@]} | tr " " "\n" | sort -u))
sortA423=($(echo ${lstA423[@]} | tr " " "\n" | sort -u))
sortA424=($(echo ${lstA424[@]} | tr " " "\n" | sort -u))

echo "A200: ${sortA200[@]}"
echo ""
echo ""

echo "A370: ${sortA370[@]}"
echo ""
echo ""

echo "A371: ${sortA371[@]}"
echo ""
echo ""

echo "A421: ${sortA421[@]}"
echo ""
echo ""

echo "A422: ${sortA422[@]}"
echo ""
echo ""

echo "A423: ${sortA423[@]}"
echo ""
echo ""

echo "A424: ${sortA424[@]}"
echo ""
echo ""

