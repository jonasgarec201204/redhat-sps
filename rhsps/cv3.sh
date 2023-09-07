#!/bin/bash
route="/etc/passwd"
while read -r line; do
	user=$(echo "$line" |cut -d":" -f1)
	bash=$(echo "$line" |cut -d":" -f7)
	name=$(echo "$line" |cut -d":" -f5)
	echo "$user $bash $name"
done < $route
exit 0
