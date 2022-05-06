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


shared_secret = 33791080262738198521897324046993048726807662844857220731500529943300369592550617340134202358359381219397666896661531845018354710691273256870990575267475221839703306931213142245169917776263826227277985171436838037171713663491373969808390932468734683976925996552387629931966621203239670064752300776053082584263655130570848359538600098589627334832078044362491796750507667269626367177928535839868002736455021645044057593023068448607539226895802034911358939773161202
iv = 'd27826513b58468479c91aaa256e9c6c'
ciphertext = 'fc152c9a0ba0cd70972ae5d68e75f2c861c955ca2937f16fcce10bba0e0044c9'

print(decrypt_flag(shared_secret, iv, ciphertext))
