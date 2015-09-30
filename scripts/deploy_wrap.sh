#!/bin/bash

export NEWVERSION=$(git rev-parse --short HEAD)

echo $NEWVERSION