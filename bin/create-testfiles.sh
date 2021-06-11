#! /bin/bash

if [ $PWD != '/tmp' ]; then
    echo "Err: please run this in the /tmp directory!"
    exit
fi

for n in {1..100}; do
    cat /dev/urandom | head -10 > file$( printf %03d "$n" ).csv
done

