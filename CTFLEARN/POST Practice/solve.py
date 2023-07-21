import requests

url = 'http://165.227.106.113/post.php'
payload = {'username': 'admin', 'password': '71urlkufpsdnlkadsf'}
res = requests.post(url, data=payload)

print(res.content)