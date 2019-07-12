#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import socket
from threading import Thread
import sys, os
import argparse, subprocess

ap = argparse.ArgumentParser()
ap.add_argument("-qr", "--qrcode", required=True, help="Path to the qrcode image")
ap.add_argument("-ip", "--server_ip", required=True, help="The server ip")
ap.add_argument("-p", "--server_port", required=True, type=int, help="The server port")
args = vars(ap.parse_args())

qr_code = subprocess.check_output(f'./qrcode_read.sh {args["qrcode"]}', shell=True).decode()[:-1]

nome = input("Nome: ")
email = input("E-mail: ")

HOST = args["server_ip"]
PORT = args["server_port"]
BUFFER = 1024

class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self):
        self.sock.connect((HOST, PORT))

        iThread = Thread(target=self.sendMsg)
        iThread.daemon = True
        iThread.start()

        while True:
            data = self.sock.recv(BUFFER)
            if not data:
                break
            print(data.decode())
            sys.exit()
  
    def sendMsg(self):
        # while True:
        self.sock.send(f'{qr_code},{nome},{email}'.encode())    

def main():
    client = Client()
main()
