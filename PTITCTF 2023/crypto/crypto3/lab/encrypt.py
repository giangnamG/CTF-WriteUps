#!/usr/bin/env python
from Crypto.PublicKey import *
from Crypto.Util.number import *
import os, sys
import socket
import threading

    
class User:
    def __init__(self, conn, addr):
        self.conn, self.addr = conn, addr
        
    def session(self):
        p, q, e, d, phin, n = self.genkey(1024)
        # Make any flag file to run this challenge
        flag = open("flag.txt").read().strip()
        self.PushStream("Welcome to RSA encryption oracle!")
        self.PushStream("Here take your flag (in hex): ", self._encrypt(flag, e, n).encode("hex"))
        self.PushStream("Here take modulus: ", n)
        
        for i in range(1050):
            self.PushStream("RSA service")
            self.PushStream("[1] Encrypt")
            self.PushStream("[2] Decrypt")
            self.PushStream("Enter your choice: ")
            option = int(self.GetStream())
            if option == 1:
                try:
                    self.PushStream("Enter the message you want to encrypt (in hex): ")
                    message = self.GetStream().decode("hex")
                except:
                    self.PushStream("Enter proper hex chars")
                    exit(0)
                ct = self._encrypt(message, e, n)
                self.PushStream("Here take your ciphertext (in hex): ", ct.encode("hex"))
                self.PushStream("\n\n")
            elif option == 2:
                try:
                    self.PushStream("Enter the ciphertext you want to decrypt (in hex): ")
                    ciphertext = self.GetStream().decode("hex")
                    
                except:
                    self.PushStream("Enter proper hex chars")
                    exit(0)
                msg = self._decrypt(ciphertext, d, n)
                self.PushStream("Here take your plaintext (in hex): ", msg.encode("hex"))
                self.PushStream("\n\n")
            else:
                self.PushStream("Enter a valid option!")
        self.PushStream("Exiting...")
    def _decrypt(self, ciphertext, d, n):
        ct = bytes_to_long(ciphertext)
        return long_to_bytes(pow(ct, d, n) % 2)

    def _encrypt(self,message, e, n):
        m = bytes_to_long(message)
        return long_to_bytes(pow(m, e, n))

    def genkey(self,size):
        p = getPrime(int(size/2))
        q = getPrime(int(size/2))
        e = 65537
        phin = (p-1)*(q-1)
        d = inverse(e, phin)
        n = p*q
        return (p, q, e, d, phin, n)
    def GetStream(self):
        return self.conn.recvall().decode('utf-8')
    
    def PushStream(self,data):
        self.conn.sendall(bytes(data+'\n','utf-8'))
    
class App:
    def __init__(self,host,port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host,port))
        self.socket.listen()
        print(f"server listening on {host}:{port}")
    
    def Listen(self):
        while True:
            try:
                conn, addr = self.socket.accept()
                new_user = User(conn, addr)
                threading.Thread(target=new_user.session).start()
            except socket.error:
                break
            
if __name__ == "__main__":
    server = App('192.168.77.1',7777)
    server.Listen()