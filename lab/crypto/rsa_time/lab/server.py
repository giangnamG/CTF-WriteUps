import socket
import threading
from Crypto.Util.number import *
import random
from sympy import isprime
import time

class RSA:
    def __init__(self, conn, addr):
        self.conn, self.addr = conn, addr
        self.my_seed = int(time.time())
        random.seed(self.my_seed)
        self.menu = '''
------------------------------------------------        
        RSA Encryption/Decryption Menu:

            1. Get Cipher
            2. Get Flag
            3. Set time
            4. Exit'''
    def session(self):
        self.PushStream(self.menu)
        while True:
            try: 
                self.PushStream("\nYour Choose: ")
                try:
                    choice = int(self.GetStream().strip())
                    if choice == 1:
                        self.GetCipher()
                    elif choice == 2:
                        self.GetFlag()
                    elif choice == 3:
                        self.SetTime()
                    else:
                        self.conn.close()
                        break
                except ValueError as e:
                    self.PushStream('error , try again !!!\n')
            except socket.error as e:
                self.conn.close()
                break
    def GetCipher(self):
        FLAG = open('./flag.txt', 'r').read()
        cipher = int.from_bytes(FLAG.encode('utf-8'),byteorder='big')
        e, n, p, q, cipher = self.encrypt(cipher)
        self.PushStream("cipher = %s\n" %str(cipher))
        self.PushStream("e = %s\n" %str(e))
        # print("p = %s\nq = %s\n" %(str(p), str(q)))
    
    def GetFlag(self):
        self.PushStream("Enter your cipher: ")
        cipher = int(self.GetStream().strip())
        self.PushStream("p = ? : ")
        p = int(self.GetStream().strip())
        self.PushStream("q = ? : ")
        q = int(self.GetStream().strip())
        self.PushStream("e = ? : ")
        e = int(self.GetStream().strip())
        try:
            n = p * q
            phi = (p-1)*(q-1)
            d = pow(e, -1, phi)
            mess = pow(cipher, d, n)
            flag = long_to_bytes(mess).decode('utf-8')
            self.PushStream(flag)
        except ValueError as e:
            self.PushStream("Wrong message !!!\n")
    
    def encrypt(self, message):
        bits = 1024
        p = self.generate_random_prime(bits)     
        q = self.generate_random_prime(bits)  
        n = p * q
        e = 65537        
        return e, n, p, q, pow(message, e, n)
    
    def SetTime(self):
        self.my_seed = int(time.time())
        random.seed(self.my_seed)
        self.PushStream("Time is up to date\n")
    
    def generate_random_prime(self, bits):
        num = random.getrandbits(bits)
        if num % 2 == 0:
                num += 1
        while True:
            if isprime(num):
                return num
            else: 
                num += 2   
    
    def GetStream(self):
        return self.conn.recv(1024).decode('utf-8')
    
    def PushStream(self, message):
        self.conn.sendall(bytes(message,'utf-8'))
        
        
class App:
    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))
        self.socket.listen()
        # print(f"server listening on {host}:{port}")        
        
    def listen(self):
        while True:
            try:
                conn, addr = self.socket.accept()
                new_user = RSA(conn, addr)
                threading.Thread(target=new_user.session).start()
            except KeyboardInterrupt as e:
                socket.close()
                break
if __name__ == '__main__':
    server = App('0.0.0.0', 7778)
    server.listen()