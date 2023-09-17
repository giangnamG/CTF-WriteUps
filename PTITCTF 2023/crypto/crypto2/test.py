a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = ['a', 'b', 'c', 'd', 'e']

for x, y in zip(a, b):
    print(x, y)
    
m = open("text.txt", "rb").read().hex()
print(m)

a = b"PTIT".hex()
b = b"CTF{".hex()
print(a+b)
m = a+b

emojis = ["😭", "😰", "😱", "😡", "😝", "😘", "😍", "😉", "😃", "😂", "😋", "😤", "😣", "😵", "😔", "😅"]
for e, c in zip(emojis, "0123456789abcdef"):
      m = m.replace(c, e)
print(m)

import emojicode
emojicode.decrypt