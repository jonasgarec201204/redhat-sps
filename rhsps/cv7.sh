#!/bin/bash
for ((i = 1 ; i < 11 ; i++)); do
	id $1$i
	if [[ $? == 0 ]]; then
                echo "uzivatel $1$i existuje"
        else
                echo "uzivatel $1$i se vytvori"
                sudo useradd $1$i
		echo -e "heslo$i\nheslo$i" |sudo passwd $1$i
        fi
done
for ((i = 1 ; i < 11 ; i++)); do
  sudo userdel -r $1$i
done
