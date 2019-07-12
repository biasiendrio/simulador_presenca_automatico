#!/bin/bash

HMAC_KEY=$1
NOME=$2
EMAIL=$3

id=`sqlite3 bd/data.db "select id_evento from evento where hmac='$HMAC_KEY';"`

if [ ! -z "$id" ]; then
	sqlite3 bd/data.db "insert into registro_presenca values(NULL,'$NOME','$EMAIL','$id');"
else
	echo "NONE"
fi