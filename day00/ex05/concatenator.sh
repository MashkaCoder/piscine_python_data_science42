#!/usr/bin/env sh

if [ $# -eq 0 ]
then
    my_path='../ex03/hh_positions.csv'
else
    my_path=$1
fi
{
  rm concatenates.csv 2>/dev/null
  head -n 1 $my_path > concatenates.csv
  for i in *[0123456789].csv
  do
    tail -n +2 $i >> concatenates.csv
  done
}
