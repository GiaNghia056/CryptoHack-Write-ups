from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')


shared_secret = 1145182537058551263848158085663066259407140837518695083035608111858056855280181251736235833007930463209957339087247148809567638648150937035992052145980725634548738522215758018029301853522374461686386170243749402710338869289821931474069230368884337005651433708358571296263899710555484377568412939069597761759507521203198806446640091050854766309938200762978514573422733822542585687672032780183577061593122276979500454331913246433949718972530045488761198765099169583
iv = 'c044059ae57b61821a9090fbdefc63c5'
ciphertext = 'f60522a95bde87a9ff00dc2c3d99177019f625f3364188c1058183004506bf96541cf241dad1c0e92535564e537322d7'

print(decrypt_flag(shared_secret, iv, ciphertext))
