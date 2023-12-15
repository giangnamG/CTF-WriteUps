''' 
Định lý euclid mở rộng: 
    Nếu gcd(a,b) = 1
    thì tổn tại 2 số (x,y) thỏa mãn:
    a*x_i + b*y_i = r_i = 1
    
Chứng minh:
    r0 = a
    r1 = b
    r2 = a%b
    q1 = a//b
    => ro = q1*r1 + r2
    => ri = q_{i+1} * r_{i+1} +r_{i+2}
    
    Hệ thức truy hồi:
        x_0, y_0 = 1, 0
            => a*1 + b*0 = a = r0
        x_1, y_1 = 0, 1
            => a*0 + b*1 = b = r1
        x_i, y_i
            => a*x_i + b*y_i = ri
        x_{i+1}, y_{i+1}
            => a*x_{i+1} + b*y_{i+1} = r_{i+1}
            
    Ta có: ri = q_{i+1} * r_{i+1} +r_{i+2}
        => r_{i+2} = ri - q_{i+1} * r_{i+1}
                   = a*x_i + b*y_i - q_{i+1} * ( a*x_{i+1} + b*y_{i+1} )
                   = a * (x_i - q_{i+1} * x_{i+1}) + b * (y_i - q_{i+1} * y_{i+1})
                   = a * x_{i+2} + b*y_{i+2}
        =>  {
                x_{i+2} = x_i - q_{i+1} * x_{i+1}
                y_{i+2} = y_i - q_{i+1} * y_{i+1}
            }
    Thuật toán dừng lại khi r_{i+2}=0
    => gcd(a,b) = r_{i+1}
    (x,y) = (x_i+1, y_i+1)
'''

def Extended_euclid(ro, r1):
    r2 = ro % r1
    q1 = ro // r1
    xo, yo = 1, 0
    x1, y1 = 0, 1
    x2, y2 = xo - q1*x1, yo - q1*y1
    
    while r2 != 0:
        ro, r1 = r1, r2
        r2 = ro % r1
        q1 = ro // r1
        xo, yo = x1, y1
        x1, y1 = x2, y2
        x2, y2 = xo - q1*x1, yo - q1*y1
    
    return r1, x1, y1

'''
Solution:
Using the two primes p = 26513, q = 32321, find the integers u,v such that
p * u + q * v = gcd(p,q)
'''
p = 26513
q = 32321
d, u, v = Extended_euclid(p,q)
print(d, u, v)