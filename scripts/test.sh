#!/bin/bash
echo "enter test"

export DEPLOYCOPY="~/DEPLOY"
export DEPLOYPATH="/home/www/py/senyu.me/deploy/"
export NEWVERSION=$(git rev-parse --short HEAD)

echo $DEPLOYCOPY
echo $DEPLOYPATH
echo $NEWVERSION

echo "leave test"