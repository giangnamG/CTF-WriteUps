import itertools

# Danh sách các ký tự bao gồm 26 chữ cái và 10 chữ số
characters = 'abcdefghijklmnopqrstuvwxyz0123456789'

# Sinh tổ hợp chập 4
combinations = itertools.combinations(characters, 4)

# In ra tất cả các tổ hợp
for combo in combinations:
    print(''.join(combo))
