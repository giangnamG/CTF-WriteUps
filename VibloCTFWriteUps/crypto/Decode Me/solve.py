from Crypto.Util.number import *
import base64, lzma

c = 'XQAAgAD//////////wApEkTrkDGPBiZf763r/fwklFegK8CapImKmYB+/m5W2+i+RYa5StHksv1q7jGZ7qUhdwUenXavwntxgUKbbKX0hkNVdU+GzMN1lZBwWHy9RFeh9xpH5tfrFV5p2yvjrrowlAr+L6a5Rmo5ssrx9KiTxyN9N85FpgT05cd12SBgE1UMkBopv4BmG7cjdSOyX0qip8otKwJ1qdJxnwfc+NB2c/TogTYsvk1l3mRiKd6DLU3eEbM89aOtH6fZqn8l/jE8fVAYKH7V7zax1TPCpvR8iaiyAdPSZGcl8RkKcN0l4kWT49flcepPJVCzqIJil1Inuj9oXgc9e/5Vg82f/AeGciy7pwfu0UayZ72MlxTp7sbjlpXCNvO9d14jozMWJe5zTns6/poPxboDROGE+/2dexhBRabB+94HZ2r4YnUzwNCcwDHNRlwujrH/ceUZfCyeAd12CAii07LZmMh8ZiGxwtbCNEE6nMW2b91Cn7JYk2Iu//+vL1Oi'
c = base64.b64decode(c)

lzd = lzma.LZMADecompressor()
decompressed_result = lzd.decompress(c)
with open('cipher.wav', 'wb+') as f:
    f.write(decompressed_result)



