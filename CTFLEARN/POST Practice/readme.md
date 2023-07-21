<h1>POST Practice</h1>

```python
import requests

url = 'http://165.227.106.113/post.php'
payload = {'username': 'admin', 'password': '71urlkufpsdnlkadsf'}
res = requests.post(url, data=payload)

print(res.content)
```
```
FLAG: flag{p0st_d4t4_4ll_d4y}
```