#!/usr/bin/env bash

function shutdown {
    echo "Shutting down"
    kill -s $1 1
    wait 5
}

function print {
    echo "Got $1 signal"
}

function loop {
    while true; do
        echo "Sleeping for 5 seconds"
        sleep 5
    done
}

trap "print TERM; shutdown TERM" TERM
trap "print KILL; shutdown KILL" KILL

loop
