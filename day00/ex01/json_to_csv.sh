#!bin/bash
if [[ $# -eq 1 ]]
then
  jq -rf filter.jq $1 > hh.csv
else
  echo "json file expected"
fi