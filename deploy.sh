#!/bin/bash

echo -e "[1] start deploy ..."
echo "origin ssh config:"
cat ~/.ssh/config
echo -e "[2] modify ssh config"
cp ~/.ssh/config_vultr ~/.ssh/config
echo -e "new ssh config:"
cat ~/.ssh/config

echo -e "\n[3] start git push ..."
git remote add production ssh://root@vultr:/opt/AdSwitcher
git push production master
echo "[4] git push completed."

echo -e "\n[5] remove remote git reop."
git remote remove production
git remote -v
echo -e "\n[6] restore ssh config"
cp ~/.ssh/config_default ~/.ssh/config
echo "origin ssh config:"
cat ~/.ssh/config
echo -e "\n[7] deploy completed."
