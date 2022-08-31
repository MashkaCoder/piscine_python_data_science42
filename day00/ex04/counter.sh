#!/usr/bin/env bash

if [[ $# -eq 0 ]]
then my_path="../ex03/hh_positions.csv"
else
  my_path=$1
fi
echo '"name","count"' > hh_uniq_positions.csv

# clean up
cat $my_path \
  | awk 'BEGIN{FS=OFS=",";} NR>1 {print $3;}' \
  | sort \
  | uniq -c \
  | awk 'BEGIN{OFS=","} {print $2, $1;}' \
  >>  hh_uniq_positions.csv
