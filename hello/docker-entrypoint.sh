#!/bin/sh

if echo $STARTUP_DELAY | grep -qE '^[0-9]+$'; then
    sleep $STARTUP_DELAY
fi

gunicorn --bind 0.0.0.0:8000 hello:app