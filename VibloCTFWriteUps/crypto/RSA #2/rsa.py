from sympy import prime
from random import getrandbits
from Crypto.Util.number import *
from gmpy2 import powmod
# from flag import flag
def primorial(n):
    P = 1
    for i in range(1, n + 1):
        P *= prime(i)
    return P

def fast_prime():
    prime = 4
    M = primorial(39)
    while not isPrime(prime):
        a = getrandbits(62)
        k = getrandbits(37)
        prime = k*M + powmod(0x10001, a, M)
    return prime
p = fast_prime()
q = fast_prime()
assert p != q, 'Wow'
n = p*q
# n = 3168542226998783506466182047102023504291529615960435044422090330277298186281086247673382335803275996903284110826148319740903322608302499363218492648058613
e = 0x10001
m = bytes_to_long(flag)
print(pow(m, e, n))
public_key = (e, n)
print (public_key)

# public_key =  65537, 3168542226998783506466182047102023504291529615960435044422090330277298186281086247673382335803275996903284110826148319740903322608302499363218492648058613
# c = 639872946051579009156510998474337005266698304204816589569626540701674347535522435948660463013516478386913922659631767939601407723744658386508524038325784