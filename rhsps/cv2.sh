#!/bin/bash
rpm -q $1
if [ $1 != 0 ]; then
	sudo dnf install -y $1
else
	exit 1
fi
read -p "Do you want to erase?(y/n)" yn
case $yn in 
	y ) echo "Erasing will begin.";;
	n ) echo "Erasing will stop, exiting.";
		exit 0;;
	* ) echo "Invalid answer, exiting.";
		exit 1;;
esac
sudo dnf erase -y $1
exit 0
