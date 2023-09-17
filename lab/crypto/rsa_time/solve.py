from pwn import *
import random, time
from sympy import isprime
from Crypto.Util.number import *

# r = remote('192.168.77.1', 7777)
r = remote('192.168.77.131', 7790)
# context.log_level = 'DEBUG'

def generate_random_prime(bits):
        num = random.getrandbits(bits)
        if num % 2 == 0:
                num += 1
        while True:
            if isprime(num):
                return num
            else: 
                num += 2   
# SET TIME
r.recv(1024)
r.send(b"3")
my_seed = int(time.time()) 
#GET CIPHER
r.send(b"1")
r.recvuntil(b"cipher")
cipher = r.recvuntil(b"e").decode("utf-8").replace('e','').replace("="," ").strip()
print("cipher = %s" %int(cipher))
e = 65537
print("e = %s" %e)
# GET FLAG

random.seed(my_seed)
p = generate_random_prime(1024)
q = generate_random_prime(1024)
r.close()
print("p = %s" %p)
print("q = %s" %q)
n = p * q
phi = (p-1)*(q-1)
d = pow(e, -1, phi)
flag = pow(int(cipher), d, n)
flag = long_to_bytes(flag).decode('utf-8')
print(flag)