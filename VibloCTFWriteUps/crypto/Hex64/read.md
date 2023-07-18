<h1>Hex64</h1>

```python
import binascii
import base64

def deHex(hex_string):
    # Chuyển đổi từ chuỗi hex thành dạng nhị phân
    binary_data = binascii.unhexlify(hex_string)
    # Chuyển đổi từ nhị phân sang văn bản
    text_data = binary_data.decode('utf-8')
    return text_data

def decode_base64(base_string):
    base64_decode = base64.b64decode(base_string).decode('utf-8')
    return base64_decode

# Đọc file hex cần giải mã
with open('./hex64','r+') as f:
     hex_string = "".join(f.readlines())
     
# Giải mã chuỗi hex thành văn bản
base64_data = deHex(hex_string) # string sau khi deHex có dạng base64
hex_string = decode_base64(base64_data)
base64_data = deHex(hex_string)
hex_string = decode_base64(base64_data)
base64_data = deHex(hex_string)
hex_string = decode_base64(base64_data)
base64_data = deHex(hex_string)
hex_string = decode_base64(base64_data)
base64_data = deHex(hex_string)
hex_string = decode_base64(base64_data)
base64_data = deHex(hex_string)
hex_string = decode_base64(base64_data)
base64_data = deHex(hex_string)
hex_string = decode_base64(base64_data)
base64_data = deHex(hex_string)
hex_string = decode_base64(base64_data)
base64_data = deHex(hex_string)
hex_string = decode_base64(base64_data)
base64_data = deHex(hex_string)
hex_string = decode_base64(base64_data)
base64_data = deHex(hex_string)
hex_string = decode_base64(base64_data)
base64_data = deHex(hex_string)
hex_string = decode_base64(base64_data)
base64_data = deHex(hex_string)
hex_string = decode_base64(base64_data)
base64_data = deHex(hex_string)
hex_string = decode_base64(base64_data)
base64_data = deHex(hex_string)
hex_string = decode_base64(base64_data)
print(hex_string)
# Flag{wow_y0u_c4n}
```
