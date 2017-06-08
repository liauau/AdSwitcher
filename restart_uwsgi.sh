#!/bin/bash
cd /opt/AdSwitcher
killall uwsgi
sleep 3s
nohup uwsgi uwsgi.ini > uwsgi.log 2>&1 &
