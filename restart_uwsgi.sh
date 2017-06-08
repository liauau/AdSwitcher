#!/bin/bash
source /opt/AdSwitcher/venv/AdSwitcher/bin/activate
killall uwsgi
sleep 3s
nohup uwsgi /opt/AdSwitcher/uwsgi.ini > /opt/AdSwitcher/uwsgi.log 2>&1 &
