from xor import bytes_xor
from base64 import*
from itertools import cycle, islice
def crack_repeating_key_xor(ct: bytes, key:bytes)-> bytes:
	full_key = islice(cycle(key),len(ct))
	return bytes_xor(ct,full_key)
def gen_key(ct:bytes, pseudo_key:bytes):
	if(len(ct)!=len(pseudo_key)):
		exit("You did it Wrong!!!")
	return bytes_xor(ct,pseudo_key)
def main():
	ct = b16decode('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104',casefold=True)
	key = gen_key(ct[:7],b'crypto{')
	print(key)
	key = key + b'y'
	print(crack_repeating_key_xor(ct,key))
if __name__=="__main__":
	main()