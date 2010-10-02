#!/bin/bash

empty_file='_empty.xml'

function remove_empty () {
    target=$1
    shift
    for i in $target/*; do
        [[ -z "`diff -q $i ${target}${empty_file}`" ]] && rm -v $i
    done
    return 0
}

remove_empty author
remove_empty coversheet
