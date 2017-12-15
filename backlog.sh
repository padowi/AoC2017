#!/bin/bash
if [ -f .meta/$USER ];
then
    find ./ -maxdepth 1 -type d -name '[012][0-9]' | grep -v -f .meta/$USER | sort
else
    echo "Please create the file .meta/$USER and on separate lines, put the directory name of each days puzzle you have solved (both a and b)"
    printf "Sample file:\n01\n03\n04\n"
    echo "This would mean that you have solved 01, 03, and 04, and they will be filtered out from this listing"
fi
