#!/bin/bash
if [ $1 == "" ]; then
	exit 1
fi
rpm -q $1
if [ $? != 0 ]; then
	sudo dnf install -y $1
else
	sudo dnf erase -y $1
fi
exit 0
