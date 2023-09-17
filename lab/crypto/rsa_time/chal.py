from Crypto.Util.number import *
import random
from sympy import isprime
import time

class RSA:
    def __init__(self):
        self.my_seed = int(time.time())
        random.seed(self.my_seed)
        self.menu = '''
------------------------------------------------        
        RSA Encryption/Decryption Menu:

            1. Get Cipher
            2. Get Flag
            3. Set time
            4. Exit'''
    def run(self):
        print(self.menu)
        while True:
            try:
                print("Your Choose: ")
                choice = int(input())
                if choice == 1:
                    self.GetCipher()
                elif choice == 2:
                    self.GetFlag()
                elif choice == 3:
                    self.SetTime()
                else:
                    break
            except ValueError as e:
                print('not in option , try again !!!')
                
    def GetCipher(self):
        FLAG = open('./flag.txt', 'r').read()
        cipher = int.from_bytes(FLAG.encode('utf-8'),byteorder='big')
        e, n, p, q, cipher = self.encrypt(cipher)
        print(f"cipher = {cipher}")
        print(f"e = {e}")
        
    def encrypt(self, message):
        bits = 1024
        p = self.generate_random_prime(bits)     
        q = self.generate_random_prime(bits)  
        n = p * q
        e = 65537        
        return e, n, p, q, pow(message, e, n)
    
    def GetFlag(self):
        try:
            cipher = int(input("Enter your cipher: ").strip())
            p = int(input("p = ? ").strip())
            q = int(input("q = ? ").strip())
            e = int(input("e = ? ").strip())
            n = p * q
            phi = (p-1)*(q-1)
            d = pow(e, -1, phi)
            mess = pow(cipher, d, n)
            flag = long_to_bytes(mess).decode('utf-8')
            print(flag)
        except ValueError as e:
            print(e)
            
    def SetTime(self):
        self.my_seed = int(time.time())
        random.seed(self.my_seed)
        print("Time is up to date")
    
    def generate_random_prime(self, bits):
        num = random.getrandbits(bits)
        if num % 2 == 0:
                num += 1
        while True:
            if isprime(num):
                return num
            else: 
                num += 2
        
if __name__ == '__main__':
    app = RSA()
    app.run()