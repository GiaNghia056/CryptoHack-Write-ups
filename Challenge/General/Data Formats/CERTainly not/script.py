from Crypto.PublicKey import RSA

with open("2048b.pem") as f:
	key = RSA.importKey(f.read())

print(key.n)