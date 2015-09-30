#!/bin/bash

echo "enter deploy_wrap"

export NEWVERSION=$(git rev-parse --short HEAD)
export DEPLOYCOPY="~/DEPLOY"
export DEPLOYPATH="/home/wwwroot/py.senyu.me/deploy/"

echo $NEWVERSION
echo $DEPLOYCOPY
echo $DEPLOYPATH
tar -zcvf ../deploy_$NEWVERSION.tar.gz * 
pwd

ll -l ./
ll -l ../

scp -i ~/.ssh/id_rsa  -o StrictHostKeyChecking=no -p 22 ../deploy_$NEWVERSION.tar.gz root@senyu.me:$DEPLOYCOPY
ssh -i ~/.ssh/id_rsa  -o StrictHostKeyChecking=no -p 22 root@senyu.me "ls -l $DEPLOYCOPY;"
ssh -i ~/.ssh/id_rsa  -o StrictHostKeyChecking=no -p 22 root@senyu.me ".remote_excute.sh $NEWVERSION $DEPLOYPATH $DEPLOYCOPY"