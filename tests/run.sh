#!/bin/bash

#############
# Functions #
#############
function httpget() {
    tempFile=$(mktemp)
    statusCode=$(curl --silent --output "$tempFile" --write-out "%{http_code}" "$1")
    returnCode=$?
    if [[ $statusCode != "200" ]]; then
        cat "$tempFile"
        rm "$tempFile"
        return $statusCode
    fi
    return $returnCode
}

# Make functions available in subshells
export -f httpget



#############
# Run tests #
#############
for test in $(find . -type f -name "test_*"); do
    echo -n "Running $test... "
    CONTAINER=$(docker run -d -p 8000:8000 0x4448/hello:dev)
    sleep 1
    output=$("$test")

    if [[ $? -eq 0 ]]; then
        echo "OK"
    else
        echo "FAIL"
        echo "$output"
    fi

    # Cleanup container
    if [[ ! -z $CONTAINER ]]; then
        docker rm -f $CONTAINER > /dev/null
    fi
    CONTAINER=""
done