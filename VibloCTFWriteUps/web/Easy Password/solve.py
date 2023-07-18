import base64
key = '5ba00d5a7ae52842c92fcd618967933a'
this_password = 'UVMEBQdSV1YGAgZQVA0NBVtdAFRSAldVXg1QB1wBC1g='
decoded_password = base64.b64decode(this_password.encode('utf-8'))
Input = "".join([chr(ord(key[i])^decoded_password[i]) for i in range(0, len(key))])
print(Input)

# Input = d1e576b71ccef5978d221fadf4f0e289 (md5)
# decrypt md5 => flag : Flag{H4r3m_n0_Jutsu}