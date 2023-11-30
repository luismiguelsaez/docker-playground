#!/usr/bin/env bash

function shutdown {
    echo "$(date '+%Y-%m-%d %H:%M:%S') [entrypoint] Shutting down processes"
    pgrep -P $$ | while read subproc
    do
        echo "$(date '+%Y-%m-%d %H:%M:%S') [entrypoint] Killing child process with PID $subproc"
        kill -s TERM $subproc
    done
    echo "$(date '+%Y-%m-%d %H:%M:%S') [entrypoint] Exiting"
}

function print {
    echo "$(date '+%Y-%m-%d %H:%M:%S') [entrypoint] Got $1 signal"
}

function loop {
    while true; do
        if [ -f /tmp/finish ]; then
            echo "$(date '+%Y-%m-%d %H:%M:%S') [entrypoint] Finish file found, exiting"
        else
            /console test1 5 &
            /console test2 10 &
            /console test3 15 &
            /console test4 20 &
            /console test5 25 &
        fi
        sleep 5
    done
}

trap "touch /tmp/finish; print TERM; shutdown TERM; exit 0" TERM
trap "touch /tmp/finish; print KILL; shutdown KILL; exit 0" KILL

loop
