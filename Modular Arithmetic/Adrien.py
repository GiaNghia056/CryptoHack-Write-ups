from random import randint
from sympy import isprime
def gcd(a , b)-> int:
    return a if b == 0 else gcd(b,a%b)
a = 288260533169915
p = 1007621497415251

FLAG = b'crypto{????????????????????}'


def encrypt_flag(flag):
    ciphertext = []
    plaintext = ''.join([bin(i)[2:].zfill(8) for i in flag])
    print(plaintext)
    for b in plaintext:
        e = randint(1, p)
        n = pow(a, e, p)
        if b == '1':
            ciphertext.append(n)
        else:
            n = -n % p
            ciphertext.append(n)
    return ciphertext

print(isprime(81267))
print(isprime(p))
print(gcd(a,p))
#print(encrypt_flag(FLAG))
