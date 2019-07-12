# Simulador de Presença Automático 
Simulador para resposta de prensença automatica em eventos.

## Pré-Requisitos 
O que precisa ser instalado para poder executar e como instalar.

* [Python 3.6+](https://www.python.org/) - Usado para executar o script.
* [qrencode](https://linux.die.net/man/1/qrencode) - Usado para a geração dos qr-codes dos eventos: ```sudo apt-get install qrencode```
* [zbar](http://zbar.sourceforge.net/) - Usado para simular o leitor de qr-code: ```sudo apt install zbar-tools```
* [sqlite3](https://www.sqlite.org/index.html) - Usado para o banco de dados dos eventos: ```sudo apt-get install sqlite3 libsqlite3-dev```

## Como executar
Para executar o script do server será necessário **CSV com lista de eventos**, **hmac key** e opcionalmente o **ip** do host se não for teste local:
> python server.py -e \<csv_file> -k \<hmac_key> \[-ip \<host>]

Para executar o script do cliente será necessário **imagem qrcode**, **host** e a **porta** do host: 
> python client.py -qr \<qrcode_img> -ip \<host> -p \<port>

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
