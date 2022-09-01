#!/usr/bin/env sh

if [ $# -eq 0 ]
then
  VACANCY='data scientist'
  echo ${VACANCY}
else
  VACANCY=$1
fi
  curl -A "chasimir" -G "https://api.hh.ru/vacancies"\
  --data-urlencode "text=${VACANCY}"\
  --data-urlencode 'page=0'\
  --data-urlencode 'per_page=20'\
  | jq > hh.json


