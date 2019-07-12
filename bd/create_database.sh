#!/bin/bash

EVENTS=$1
export IFS=","

mkdir qrcodes &> /dev/null

# drop tabela
sqlite3 bd/data.db < bd/drop.sql

# cria tabela 
sqlite3 bd/data.db < bd/create.sql

# insere eventos na tabela de eventos e cria os qrcodes
while read nome_evento data_evento hora_ini hora_fim local observacao; do 
	HMAC=`echo "$nome_evento $data_evento $hora_ini $hora_fim $local $observacao" | openssl dgst -sha1 -hmac $2 | awk '{print $2}'`
	sqlite3 bd/data.db "insert into evento values(NULL, '$HMAC' , '$nome_evento', $data_evento, '$hora_ini', '$hora_fim', '$local', '$observacao');"

	qrencode -o "qrcodes/$nome_evento.png" $HMAC
done < "$EVENTS"


