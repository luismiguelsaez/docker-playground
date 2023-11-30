#!/usr/bin/env bash

function shutdown {
    echo "$(date '+%Y-%m-%d %H:%M:%S') [$CMD] Shutting down process"
    sleep 5
}

function print {
    echo "$(date '+%Y-%m-%d %H:%M:%S') [$CMD] Got $1 signal"
}

function run {
    echo "$(date '+%Y-%m-%d %H:%M:%S') [$CMD] Running command"
    sleep $2
    echo "$(date '+%Y-%m-%d %H:%M:%S') [$CMD] Ending command"
}

trap "print TERM; sleep 5; shutdown; exit 0" TERM

CMD=$1
TIMEOUT=$2

run $CMD $TIMEOUT
