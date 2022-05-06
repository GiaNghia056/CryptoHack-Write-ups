def quadratic_residue(x:int, p: int):
	for i in range(p):
		if(i**2 % p == x):
			return (-i,i)
p = 29
ints = [14, 6, 11]
qr = [a for a in range(p) if pow(a,2,p) in ints]
print(f"flag : {min(qr)}")
