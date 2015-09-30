#!/bin/bash

export NEWVERSION=$(git rev-parse --short HEAD)
export DEPLOYCOPY="~/DEPLOY"
export DEPLOYPATH="/home/www/py/senyu.me/deploy/"

echo $NEWVERSION

tar -zcvf ../deploy_$NEWVERSION.tar.gz * 

scp -i ~/.ssh/id_rsa  -o StrictHostKeyChecking=no -p 22 ../deploy_$NEWVERSION.tar.gz root@senyu.me:$DEPLOYCOPY
ssh -i ~/.ssh/id_rsa  -o StrictHostKeyChecking=no -p 22 root@senyu.me ".remote_excute.sh $NEWVERSION $DEPLOYPATH $DEPLOYCOPY"