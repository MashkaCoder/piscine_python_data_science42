 #!bin/bash
 if [$# -eq 0]
  then
   VACANCY = 'data scientist'
  else
    VACANCY = $1
 fi
   curl -A "chasimir" -G "https://api.hh.ru/vacancies"\
   --data-urlencode 'per_page=20'\
   --data-urlencode 'page=0'\
   --data-urlencode "search_field=name"\
   --data-urlencode "text=${VACANCY}"\
   | jq > hh.json

#   | jq '.' hh.json > hh.json
# curl -o hh.json -A "chasimir" -G "https://api.hh.ru/vacancies"\
#   --data-urlencode 'per_page=20'\
#   --data-urlencode 'page=0'\
#   --data-urlencode "search_field=name"\
#   --data-urlencode "text=${VACANCY}"\
#   | jq > hh.json