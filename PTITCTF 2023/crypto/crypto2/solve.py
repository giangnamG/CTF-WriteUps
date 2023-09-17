import ast
import random

def generate_permutations(emojis, index, length):
    if index == length:
        emojis_[1] = emojis_lose[0]
        emojis_[2] = emojis_lose[1]
        emojis_[8] = emojis_lose[2]
        emojis_[10] = emojis_lose[3]
        emojis_[12] = emojis_lose[4]
        emojis_[14] = emojis_lose[5]
        emojis_[15] = emojis_lose[6]
        print(''.join(emojis_))
        flag = decode(cipher, emojis_)
        print(flag)
        if flag:
            if "1nv1s1bl3_k1ll3r" in flag:
                return
    else:
        for i in range(index, length):
            emojis[index], emojis[i] = emojis[i], emojis[index]
            generate_permutations(emojis, index + 1, length)
            emojis[index], emojis[i] = emojis[i], emojis[index]

def decode(cipher, emojis):
    try:
        for e, c in zip(emojis, "0123456789abcdef"):
            cipher = cipher.replace(e, c)
        return bytes.fromhex(cipher).decode('utf-8')
    except:
        pass

# emojis = ["😭", "😰", "😱", "😡", "😝", "😘", "😍", "😉", "😃", "😂", "😋", "😤", "😣", "😵", "😔", "😅"]
emojis_ = ['😡','','','😉','😃','😣','😂','😍','','😝','','😔','','😱','','']

emojis_lose = ["😭","😰","😘","😋","😤","😵","😅"]

for _ in emojis_:
    if _ != '':
        _ = hex(ord(_))
        print(_)
        
for _ in emojis_lose:
    _ = hex(ord(_))
    print(_)
    
with open("out.txt", "r") as file:
    cipher = file.read()
for _ in cipher:
    _ = hex(ord(_))

    
# generate_permutations(emojis_lose, 0, len(emojis_lose))
