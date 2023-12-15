from Crypto.Util.number import inverse, long_to_bytes

n = 1522605027922533360535618378132637429718068114961380688657908494580122963258952897654000350692006139
c = 1292388824308250413889931565779670794681429363528473914956124924973851952746553591901513127456003320

p = 37975227936943673922808872755445627854565536638199
q = 40094690950920881030683735292761468389214899724061

assert n == p * q

phi = (p - 1) * (q - 1)
m = None
# d = inverse(3, phi)
# m = long_to_bytes(pow(c, d, n)).decode('utf-8')

for e in range(10**4, 10 ** 7):
    try:
        print(e)
        d = pow(e, -1, phi)
        m = long_to_bytes(pow(c, d, n)).decode('utf-8')
        break  # Break out of the loop once decryption is successful
    except ValueError:
        continue  # If inverse is not possible, try the next value of e

print(m)
