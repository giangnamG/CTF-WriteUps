from Crypto.Util.number import *
from Crypto.PublicKey import RSA
from pwn import *
import time

r = remote("128.199.247.205", 6989)
# context.log_level = 'DEBUG'
flag_enc = int(r.recvline().decode()[10:].strip())
e = int(r.recvline().decode()[3:].strip())
n = int(r.recvline().decode()[3:].strip())
length = int(r.recvline().decode()[7:].strip())

# flag_enc = 4134068372664388797267781289500557662149037923540618091170266626388628321274369947005295116381084550663227737043809101779327798796397946201599730540584729298862083672473402888853985256864640694486388257573197458294489189539102368594553212309038930571394905111102460774554871630008651099155931698554756850834514908529344129801061907427280888859438549178669406427982190853717014787575037404605528731409418219346367673734691723765767584159462031385000328590725385091002678117745061793560881305329791952697494620903637356539385078595035005094992080193265320332303593719549021940145556705406071693519507646994458525566208
# e = 65537
# n = 21707984294808419379145651046029775788321499130493081482585763442873220866420305290199288315785045866783385436098685220534307242163399223935905846910274853111750615292893728720520266024797324101171182392258264396833738206762299797114721973762576207997183268587735801254573275460306907282464938293615898323762358475437137219968700940914179265896700589812448299890707197964410245644096932613419633932274580898805804685154060732170339128999468156023966065302653192551679273334285478764862991433096758615157127782781120226881591435503889217614038981783221413493811388121576614715528964403085497933397353585531200208885781
# length = 671
print(f"flag_enc = {flag_enc}")
print(f"e = {e}")
print(f"n = {n}")
print(f"length = {length}")

def decrypt(cipher):
    r.recvuntil(b"c = ")
    r.sendline(str(cipher).encode("utf-8"))
    plan_text = int(r.recvline().decode()[7:].strip())
    return plan_text

def last_bit(upper_limit, lower_limit, last_byte):
    if last_byte == 0:
            upper_limit = (upper_limit + lower_limit) // 2
    elif last_byte == 1:
        lower_limit = (lower_limit + upper_limit) // 2 + 1
    elif last_byte == 2:
        upper_limit = (upper_limit + lower_limit) // 2
    elif last_byte == 3:
        lower_limit = (lower_limit + upper_limit) // 2 + 1
    elif last_byte == 4:
        lower_limit = (lower_limit + upper_limit) // 2 + 1
    return upper_limit, lower_limit
    
upper_limit = n
lower_limit = 0    
flags = []
i = 1
Max = n.bit_length()

while i <= Max:
    try:
        inv = inverse(5*i, n)
        chosen_ct = (flag_enc * pow(inv, e, n)) % n
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