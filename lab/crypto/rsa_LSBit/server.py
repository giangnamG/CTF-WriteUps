from Crypto.Util.number import *

# p = getPrime(512)
# q = getPrime(512)
# e = 65537
p = 7
q = 13
e = 5
n = p * q
phi = (p - 1)*(q - 1)
d = pow(e, -1, phi)

flag = "PTITCTF{asd_kjdf_sdhf}"
flag = bytes_to_long(flag.encode())

def encrypt(message):
    return pow(message, e, n)

def decrypt(cipher):
    return pow(cipher, d, n)

cipher = encrypt(flag)
last_bit = decrypt(cipher)

# c_of_2 = encrypt(2)
# c_of_5 = encrypt(5)

# print(f"c_of_2: {c_of_2}")
# print(f"c_of_5: {c_of_5}")
# c_of_2x5 = encrypt(c_of_2*c_of_5)
# print(f"c_of_2x5: {c_of_2x5}")
# m_of_2x5 = decrypt(decrypt(c_of_2x5))
# print(f"m_of_2x5: {m_of_2x5}")
c = decrypt(2)
print(c)
print(encrypt(c))