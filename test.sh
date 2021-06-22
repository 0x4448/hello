#!/bin/bash -e

# Build and test container.

function cleanup() {
    if [[ ! -z $CONTAINER ]]; then
        docker rm -f $CONTAINER
    fi
    if [[ -z "$1" ]]; then
        exit 1
    fi
    echo "$1"
}

trap cleanup ERR

docker build --tag 0x4448/hello:dev .
CONTAINER=$(docker run -d -p 8000:8000 0x4448/hello:dev)
sleep 1
curl http://127.0.0.1:8000
cleanup OK