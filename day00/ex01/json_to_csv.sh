#!/usr/bin/env bash
if [[ $# -eq 0 ]]
then
  my_path="../ex00/hh.json"
else
  my_path=$1
fi
  jq -rf filter.jq ${my_path} > hh.csv