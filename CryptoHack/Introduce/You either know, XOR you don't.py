'''
solution:
I've encrypted the flag with my secret key, you'll never be able to guess it.
Remember the flag format and how it might help you in this challenge!

0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104
'''
from itertools import cycle
enc = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

print(enc)
flag = "crypto{"
key = ""
for f,e in zip(flag, enc):
    key += chr(ord(f)^e)
key += chr(ord("}")^enc[len(enc)-1])
print(key)
key = cycle(key)
for e, k in zip(enc, key):
    print(chr(e^ord(k)), end='')
