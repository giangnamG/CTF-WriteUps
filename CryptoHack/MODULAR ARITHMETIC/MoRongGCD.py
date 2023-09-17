'''
Cho 2 số dương a, b
Thuật toán Euclide mở rộng là một cách hiệu quả để tìm các số nguyên u,v sao cho:
    a * u + b * v = gcd(a,b)

Sử dụng hai số nguyên tố p = 26513, q = 32321, tìm các số nguyên u,v sao cho:
    p * u + q * v = gcd(p,q)

Biết rằng p,q là số nguyên tố, bạn mong đợi gcd(p,q) sẽ là bao nhiêu?
tham khảo: https://web.archive.org/web/20230511143526/http://www-math.ucdenver.edu/~wcherowi/courses/m5410/exeucalg.html
'''
def gcd(a, b):
    while b:
        x = a%b
        a = b
        b = x
    return a
p = 26513
q = 32321
u = gcd(p, q)
print(u)
