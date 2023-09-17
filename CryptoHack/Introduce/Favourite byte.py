'''
solution:
For the next few challenges, you'll use what you've just learned to solve some more XOR puzzles.

I've hidden some data using XOR with a single byte, but that byte is a secret. Don't forget to decode from hex first.

73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d
'''
enc = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
print(enc)
for byte in range(100):
    mess = "".join([chr(x^byte) for x in enc])
    if "crypto" in mess:
        print(mess)
