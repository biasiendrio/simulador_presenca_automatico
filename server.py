#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import socket
from threading import Thread
import argparse, subprocess
import os

ap = argparse.ArgumentParser()
ap.add_argument("-e", "--events", required=True, help="Path to the CSV withe the events list")
ap.add_argument("-k", "--hmac_key", required=True, help="The hmac key to generate qrcode")
ap.add_argument("-ip", "--host", help="Ip of the host")
args = vars(ap.parse_args())

os.system(f'./bd/create_database.sh {args["events"]} {args["hmac_key"]}')

HOST = '127.0.0.1' 
if args["host"]:
    HOST = args["host"]
BUFFER = 1024

class Server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conexoes = list()
    PORT = 5000

    def __init__(self):
        self.start_bind()   
        self.sock.listen(1)

    def start_bind(self):
        teste = True
        while teste:
            try:
                self.sock.bind((HOST,self.PORT))
                teste = False
            except:
                self.PORT += 1
    
    def envio(self, conteudo, infos):
        try:
            while True:
                data = conteudo.recv(BUFFER)
                if data:
                    dados_participante = data.decode().split(',')                    
                    qrcode_certo = subprocess.check_output(f'./adiciona_presenca.sh {dados_participante[0]} {dados_participante[1]} {dados_participante[2]}',
                                                    shell=True).decode()[:-1]
                    if qrcode_certo == "NONE":
                        conteudo.send('Error qrcode'.encode())
                    else:
                        conteudo.send('Presença registrada'.encode())

                else:
                    print('Desconectado porta: {}'.format(infos[1]))
                    self.conexoes.remove(conteudo)
                    conteudo.close()                
        except:
            pass
    
    def executa(self):
        print('Start Server...')
        print(f'IP Server: {HOST} | PORT Server: {self.PORT}')
        try:
            while True: 
                conteudo, infos = self.sock.accept()
                conn = Thread(target=self.envio, args=(conteudo,infos))
                conn.daemon = True
                conn.start()
                self.conexoes.append(conteudo)
                print(f'Conectado porta: {infos[1]}')
        except:
            pass
            
def main():
    server = Server()
    server.executa()
main()
