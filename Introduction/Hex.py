from base64 import*
s = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
s = b16decode(s.upper())
print(s)
print(b64encode(s))