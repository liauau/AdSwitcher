#!/bin/bash
cd /opt/AdSwitcher
source ./venv/AdSwitcher/bin/active
killall uwsgi
sleep 3s
nohup uwsgi uwsgi.ini > uwsgi.log 2>&1 &
