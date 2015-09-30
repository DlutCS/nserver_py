#!/bin/bash

echo "enter deploy_wrap"

export DEPLOYPROJECTNAME="nserverPy"
export NEWVERSION=$(git rev-parse --short HEAD)
export DEPLOYCOPY="~/DEPLOY/"
export DEPLOYDEST="/home/wwwroot/py.senyu.me/deploy/"
export DEPLOYFILENAME=deploy_${DEPLOYPROJECTNAME}_${NEWVERSION}.tar.gz
export DEPLOYSERVER="root@senyu.me"

echo $DEPLOYPROJECTNAME
echo $NEWVERSION
echo $DEPLOYCOPY
echo $DEPLOYDEST
echo $DEPLOYFILENAME
echo $DEPLOYSERVER

tar -zcf ../$DEPLOYFILENAME * --exclude=venv --exclude=ci_scripts

scp -i ~/.ssh/id_rsa  -o StrictHostKeyChecking=no -p 22 ../${DEPLOYFILENAME} ${DEPLOYSERVER}:${DEPLOYCOPY}
#ssh -i ~/.ssh/id_rsa  -o StrictHostKeyChecking=no -p 22 $DEPLOYSERVER "ls -l $DEPLOYCOPY;"
ssh -i ~/.ssh/id_rsa  -o StrictHostKeyChecking=no -p 22 ${DEPLOYSERVER} "${DEPLOYCOPY}/remote_execute.sh ${NEWVERSION} ${DEPLOYCOPY} ${DEPLOYDEST} ${DEPLOYPROJECTNAME} ${DEPLOYFILENAME}"