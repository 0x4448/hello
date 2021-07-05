#!/bin/bash

#############
# Functions #
#############
function get() {
    # Parameters:
    # $1: URI
    # $2: expected response status code
    tempFile=$(mktemp)
    statusCode=$(curl --silent --output "$tempFile" --write-out "%{response_code}" "$1")
    rm "$tempFile"
    if [[ $statusCode -ne $2 ]]; then
        return 1
    fi
}


#############
# Run tests #
#############
successURIs=(
    http://localhost:8000
    http://localhost:8000/env
    http://localhost:8000/probes/live
    http://localhost:8000/probes/ready
    http://localhost:8000/probes/startup
)

for uri in ${successURIs[@]}; do
    echo -n "Checking $uri ... "
    get $uri 200
    if [[ $? -eq 0 ]]; then
        echo "OK"
    else
        echo "FAIL"
    fi
done
