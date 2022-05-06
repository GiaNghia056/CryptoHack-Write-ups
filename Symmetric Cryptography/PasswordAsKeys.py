from base64 import b16decode,b16encode
import requests
import hashlib
import random
BASE_URL = "http://aes.cryptohack.org/passwords_as_keys"

# 1) get the ciphertext of the encrypted flag
r = requests.get(f"{BASE_URL}/encrypt_flag/")
data = r.json()
ciphertext = data["ciphertext"]
#print("ciphertext", ciphertext)
cnt = 1
with open("PasK.txt") as f:
    words = [w.strip() for w in f.readlines()]
def decrypt(word):
    keyword = word
    KEY = hashlib.md5(keyword.encode()).digest()
    KEY = b16encode(KEY).decode().lower()
    #print(KEY)
    # 2) send the ciphertext to the decrypt function
    r = requests.get(f"{BASE_URL}/decrypt/{ciphertext}/{KEY}")
    data = r.json()
    plaintext = data["plaintext"]
    # 3) convert from hex to ASCII to have the flag
    #plaintext = b16decode(plaintext.upper())
    print("flag", b16decode(plaintext.upper()))
for s in words:
    decrypt(s)
#b'xd<\xcb\x90X\x02\x80\xa8\xdc\xc4\x15\xe0\x0c\x0b>8\x99l\x1e\xb7&E\xb2\xcd\xaf\x05\xf4\xc9\x19\x9f\x92'