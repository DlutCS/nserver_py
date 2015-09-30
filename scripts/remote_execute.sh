#!/bin/bash


NEWVERSION=$1
DEPLOYPATH=$2
DEPLOYCOPY=$3

cd $DEPLOYCOPY
mv ./deploy_$NEWVERSION.tar.gz $DEPLOYPATH
cd $DEPLOYPATH
mkdir -p $NEWVERSION
tar -zxvf $deploy_$NEWVERSION.tar.gz -C $NEWVERSION
cd ./$NEWVERSION

pwd
ll ./
#修改一下uwsgi.ini

