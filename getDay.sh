#!/bin/bash

while getopts "y:d:t" option; do
    case $option in
        y) year=$OPTARG;;
        d) day=$OPTARG
           if [ ${#day} -eq 1 ]; then
              day="0$day"
           fi;;
        t) year=$(date '+%Y')
           day=$(date '+%d');;
        \?) echo "Unkown inputs"
            exit;;
    esac
done

if [ -z ${year+x} ]; then
    echo "year not defined"
fi

if [ -z ${day+x} ]; then
    echo "day not defined"
fi

if [ -z ${day+x} ] || [ -z ${year+x} ]; then
    exit;
fi

link="https://adventofcode.com/$year/day/${day##0}/input"

if [[ ! -d "$year" ]]; then
   mkdir $year
   echo "folder $year created"
fi
dir="$year/Day$day"
if [[ ! -d $dir ]]; then
    mkdir $dir
    echo "folder $dir created"
fi

if [[ ! -f "$dir/Day${day}in.txt" ]]; then
    touch "${dir}/Day${day}in.txt"
    echo "file ${dir}/Day${day}in.txt created"
    curl $link -b "cookie.txt" -o "$dir/Day${day}in.txt"
fi

if [[ ! -f "$dir/Day${day}.py" ]]; then
    touch "${dir}/Day${day}.py"
    echo "file ${dir}/Day${day}.py created"
fi



