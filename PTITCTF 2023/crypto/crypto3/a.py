from Crypto.Util.number import *
from Crypto.PublicKey import RSA

flag = open("flag.txt", "r").read().strip()
flag = bytes_to_long(flag.encode())
key = RSA.generate(2048)
e = key.e
p = key.p
q = key.q
n = key.n
d = key.d
flag_enc = pow(flag, e, n)
print("flag_enc = " + str(pow(flag, e, n)))
print("e = " + str(e))
print("n = " + str(n))
print("Length: " + str(len(bin(flag)[2:])))

flags = []
i = 1
Max = n.bit_length()
def decrypt(cipher):
    m = pow(c, d, n)
    return m % 5

def last_bit(upper_limit, lower_limit, last_byte):
    if last_byte == 0:
            upper_limit = (upper_limit + lower_limit) // 2
    elif last_byte == 1:
        lower_limit = (lower_limit + upper_limit) // 2 + 1
    elif last_byte == 2:
        upper_limit = (upper_limit + lower_limit) // 2
    elif last_byte == 3:
        lower_limit = (lower_limit + upper_limit) // 2
    elif last_byte == 4:
        lower_limit = (lower_limit + upper_limit) // 2
    return upper_limit, lower_limit

while i <= Max:
    try:
        chosen_ct = (flag_enc * pow(2 ** i, e, n)) % n
        print(f"New cipher: {chosen_ct}")
        output = decrypt(chosen_ct)
        print(f"last bit: {output}")
        upper_limit, lower_limit = last_bit(upper_limit, lower_limit, output)
        flags.append(long_to_bytes(lower_limit))
        # try:
        print(f"Flag: %s" %long_to_bytes(lower_limit))
        # except :
        #     pass
        i+=1
    except :
        break

for _ in flags:
    print("start")
    try:
        print(f"Flag: %s" %_.decode('utf-8'))
    except :
        pass
limit = 100 + len(bin(flag)[2:])
for i in range(limit):
    try:
        c = int(input('c = '))
        m = pow(c, d, n)
        print("Result: " + str(m % 5))
    except:
        exit(0)