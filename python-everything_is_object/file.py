#!/usr/bin/bash

filename="-answer"
ext="txt"
num=28
while [ $num -gt -1 ]; do
    fname=$num$filename.$ext
    touch "$fname"
    ((num--))
done
