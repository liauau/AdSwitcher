#!/bin/bash
UWSGI_PORT=$1
PID=$(lsof -i:$UWSGI_PORT | tail -1 | awk '{ print $2}')

if [  $# -ne 1 ]; then
    echo 'usage: restart_uwsgi.sh [port_number]'
    exit
fi

if [ $UWSGI_PORT = 8001 ]; then
    cd /opt/AdSwitcher
else
    echo 'The port number is not valid'
    exit
fi

kill -- -$(ps -o pgid= $PID | grep -o '[0-9]*')
pwd
sleep 3s
nohup uwsgi uwsgi.ini > uwsgi.log 2>&1 &
