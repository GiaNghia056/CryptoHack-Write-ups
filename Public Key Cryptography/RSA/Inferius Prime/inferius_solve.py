n = 742449129124467073921545687640895127535705902454369756401331
e = 3
ct = 39207274348578481322317340648475596807303160111338236677373
from factordb.factordb import FactorDB
from Crypto.Util.number import long_to_bytes,inverse
f = FactorDB(n)
f.connect()
factor = f.get_factor_list()
phi = 1
for i in factor:
	phi*=(i-1)
d = inverse(e,phi)
print(long_to_bytes(pow(ct,d,n)))