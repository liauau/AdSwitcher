#!/bin/bash
if [ $# -ne 1 ] || [ $1 != 'debug' ] && [ $1 != 'production' ]; then
    echo 'usage: ./deploy.sh [debug|production]'
    exit
fi

env=$1

echo -e "[1] start deploy ..."
echo "origin ssh config:"
cat ~/.ssh/config
echo -e "[2] modify ssh config"
cp ~/.ssh/config_vultr ~/.ssh/config
echo -e "new ssh config:"
cat ~/.ssh/config

echo -e "\n[3] start git push ..."
remote_repo='ssh://root@vultr:/opt/AdSwitcher'

if [ $1 = 'debug' ]; then
    remote_repo='ssh://root@vultr:/opt/Debug_AdSwitcher'
fi
echo 'push to '$remote_repo
git push $remote_repo master
echo "[4] git push completed."

echo -e "\n[5] restore ssh config"
cp ~/.ssh/config_default ~/.ssh/config
echo "origin ssh config:"
cat ~/.ssh/config
echo -e "\n[6] deploy completed."
