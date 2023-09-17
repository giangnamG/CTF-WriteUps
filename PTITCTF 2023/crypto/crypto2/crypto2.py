import random

emojis = ["😭", "😰", "😱", "😡", "😝", "😘", "😍", "😉", "😃", "😂", "😋", "😤", "😣", "😵", "😔", "😅"]

print(len(emojis))
m = open("text.txt", "rb").read().hex()

# random.shuffle(emojis)
print(emojis)

for e, c in zip(emojis, "0123456789abcdef"):
    m = m.replace(c, e)
print(m)
# open("out_test.txt", "w").write(m)
