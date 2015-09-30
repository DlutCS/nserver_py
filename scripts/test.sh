#!/bin/bash

export NEWVERSION=$(git rev-parse --short HEAD)
export DEPLOYCOPY="~/DEPLOY"
export DEPLOYPATH="/home/www/py/senyu.me/deploy/"

echo $NEWVERSION
echo $DEPLOYCOPY
echo $DEPLOYPATH