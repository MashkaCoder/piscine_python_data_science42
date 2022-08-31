 #!/bin/bash
if [[ $# -eq 0 ]]
then my_path="../ex02/hh_sorted.csv"
else
  my_path=$1
fi
head -n 1 ${my_path} > hh_positions.csv
tail -n 20 ${my_path} | \
awk 'BEGIN { FS = OFS = "," }
    {
        STR = ""
        if (index(tolower($3), "junior"))
            STR = STR"Junior/"
        if (index(tolower($3), "middle"))
            STR = STR"Middle/"
        if (index(tolower($3), "senior"))
            STR = STR"Senior"
        if (STR == "")
            STR = "-"
        gsub(/[\/ ]*$/, "", STR)
        
        $3 = "\""STR"\""
        print
    }' \
    >> hh_positions.csv