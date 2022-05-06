from base64 import*
def bytes_xor(a:bytes, b:bytes):
	return bytes(byte_1 ^ byte_2 for byte_1,byte_2 in zip(a,b))
def int_xor(a:bytes, b: int):
	return bytes(byte ^ b for byte in a)
if __name__=="__main__":
	a = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'.upper()
	b = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'.upper()
	c = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'.upper()
	d = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'.upper()
	a,b,c,d = map(b16decode,(a,b,c,d))
	key1 = a
	key2 = bytes_xor(b,key1)
	key3 = bytes_xor(c,key2)
	key = bytes_xor(c,key1)
	key = bytes_xor(d,key)
	print(key)