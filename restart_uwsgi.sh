killall uwsgi
cd /opt/AdSwitcher
pwd
sleep 3s
nohup uwsgi uwsgi.ini > uwsgi.log 2>&1 &
