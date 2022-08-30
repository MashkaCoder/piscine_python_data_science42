 #!bin/bash
if [[ $# -eq 0 ]]
then
  my_path="../ex01/hh.csv"
else
  my_path=$1
fi
(head -n 1 ${my_path}; tail -n 20 ${my_path} | sort -t ',' -k 2 -k 1n) > hh_sorted.csv

