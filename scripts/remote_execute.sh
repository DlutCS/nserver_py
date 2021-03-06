#!/bin/bash

NEWVERSION=$1
DEPLOYCOPY=$2
DEPLOYDEST=$3
DEPLOYPROJECTNAME=$4
DEPLOYFILENAME=$5
DEPLOYMODE=$6

DEPLOYOUTPUTDIR=${DEPLOYPROJECTNAME}_${NEWVERSION}

echo "cd ${DEPLOYCOPY}"
cd ${DEPLOYCOPY}
echo "cp -f ${DEPLOYFILENAME} ${DEPLOYDEST}"
cp -f ${DEPLOYFILENAME} ${DEPLOYDEST}
echo "cd ${DEPLOYDEST}"
cd ${DEPLOYDEST}
echo "mkdir -p ${DEPLOYOUTPUTDIR}"
mkdir -p ${DEPLOYOUTPUTDIR}
echo "tar -zxvf ${DEPLOYFILENAME} -C ${DEPLOYOUTPUTDIR}"
tar -zxvf ${DEPLOYFILENAME} -C ${DEPLOYOUTPUTDIR}
echo "ln -sf ${DEPLOYOUTPUTDIR} current"
ln -sfT ${DEPLOYOUTPUTDIR} current

echo "cd current"
cd current

if [ ${DEPLOYMODE} = "PRODUCTION" ]; then
	echo "make DEPLOYOUTPUTDIR=${DEPLOYDEST}/current PRODUCTION='TRUE'"
	make DEPLOYOUTPUTDIR=${DEPLOYDEST}/current PRODUCTION='TRUE'
elif [ ${DEPLOYMODE} = "PRELEASE" ]; then
	echo "make DEPLOYOUTPUTDIR=${DEPLOYDEST}/current PRELEASE='TRUE'"
	make DEPLOYOUTPUTDIR=${DEPLOYDEST}/current PRELEASE='TRUE'
fi

