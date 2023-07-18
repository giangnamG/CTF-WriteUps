<h1>Mã Morse Kì Lạ</h1>

```python
def decode_morse_code(morse_code):
    morse_dict = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
                  '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
                  '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
                  '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
                  '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
                  '--..': 'Z', '-----': '0', '.----': '1', '..---': '2',
                  '...--': '3', '....-': '4', '.....': '5', '-....': '6',
                  '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.',
                  '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!',
                  '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&',
                  '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+',
                  '-....-': '-', '..--.-': '_', '.-..-.': '"', '...-..-': '$',
                  '.--.-.': '@', '...---...': 'SOS'}
    morse_code = morse_code.split(' ')
    decoded_text = ''
    for symbol in morse_code:
        if symbol in morse_dict:
            decoded_text += morse_dict[symbol]
        else:
            decoded_text += ' '
    return decoded_text


cipher = 'YYXY YXYY YX XXY { X YYYY Y _ XX XXX YXY YYY Y _ XYXX XXX YYX _ XYX XY XXX YXX _ X YYYY Y _ XX XXX YXY Y _ XYXX XXX YYX _ XYX XY XXX YXX }'
morse_code = cipher.replace("Y",".").replace("X","-")
print(morse_code)
flag = decode_morse_code(morse_code)
print(flag.lower())

```
>..-. .-.. .- --. { - .... . _ -- --- .-. ... . _ -.-- --- ..- _ -.- -. --- .-- _ - .... . _ -- --- .-. . _ -.-- --- ..- _ -.- -. --- .-- }

> Flag{the_morse_you_know_the_more_you_know}