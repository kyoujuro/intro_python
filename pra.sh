#!/bin/bash
<< COMMENTOUT
Practice
COMMENTOUT
name="hoge"
echo "hello $name"
read -p "your name is: " your_name
echo "hello $your_name"
count=1
echo  $(( ${count} + 1))
if (( $count > 0 )); then
    echo "OK"
else 
    echo "NG"
fi

