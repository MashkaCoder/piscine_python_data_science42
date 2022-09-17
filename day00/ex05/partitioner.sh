#!/usr/bin/env sh

if [ $# -eq 0 ]
then
    my_path='../ex03/hh_positions.csv'
else
    my_path=$1
fi
{
    cat $my_path \
    | awk ' BEGIN { FS = "\",\"|T" }
        {
            if (NR == 1)
                START = $0
            else
            {
                if (!($2 in files))
                {
                    file = $2".csv"
                    files[$2]
                    print START > file
                }
                print >> file
            }
        }
        ' $1
}



