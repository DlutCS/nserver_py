#!/bin/bash

echo "enter deploy_wrap"

DEPLOYPROJECTNAME="nserverPy"
NEWVERSION=$(git rev-parse --short HEAD)
DEPLOYCOPY="~/DEPLOY/"
DEPLOYDEST="/home/wwwroot/py.senyu.me/deploy/"
DEPLOYFILENAME=deploy_${DEPLOYPROJECTNAME}_${NEWVERSION}.tar.gz
DEPLOYSERVER="deploy@senyu.me"
DEPLOYMODE="PRODUCTION"

echo $DEPLOYPROJECTNAME
echo $NEWVERSION
echo $DEPLOYCOPY
echo $DEPLOYDEST
echo $DEPLOYFILENAME
echo $DEPLOYSERVER

tar -zcf ../$DEPLOYFILENAME * --exclude=venv --exclude=scripts

scp -i ~/.ssh/id_rsa  -o StrictHostKeyChecking=no -p 22 ../${DEPLOYFILENAME} ${DEPLOYSERVER}:${DEPLOYCOPY}
#ssh -i ~/.ssh/id_rsa  -o StrictHostKeyChecking=no -p 22 $DEPLOYSERVER "ls -l $DEPLOYCOPY;"
ssh -i ~/.ssh/id_rsa  -o StrictHostKeyChecking=no -p 22 ${DEPLOYSERVER} "${DEPLOYCOPY}/remote_execute.sh ${NEWVERSION} ${DEPLOYCOPY} ${DEPLOYDEST} ${DEPLOYPROJECTNAME} ${DEPLOYFILENAME} ${DEPLOYMODE}"