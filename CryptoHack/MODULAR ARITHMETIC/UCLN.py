'''
- Thuật toán Euclide dựa trên nguyên tắc ước chung lớn nhất của hai số không thay đổi nếu số lớn hơn được thay thế bằng hiệu của nó với số nhỏ hơn.

- Nếu gcd(a, b) = 1 thì a và b được gọi là nguyên tố cùng nhau
- Đặt g = gcd(a, b). Vì a và b đều là bội số của g nên chúng có thể được viết là a = mg và b = ng và không có số nào lớn hơn G > g mà điều này đúng. 
    Các số tự nhiên m và n phải nguyên tố cùng nhau, vì bất kỳ ước số chung nào cũng có thể được tách ra khỏi m và n để làm cho g lớn hơn
    
gcd(a, b, c) = gcd(a, gcd(b, c)) = gcd(gcd(a, b), c) = gcd(gcd(a, c), b).
'''

def gcd(a, b):
    while b:
        x = a%b
        a = b
        b = x
    return a
print(gcd(1071,462))