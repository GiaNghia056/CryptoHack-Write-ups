from math import*
def extended_gcd(x:int, n:int)->tuple[int,int]:
	ox = x
	on = n
	r = gcd(x,n)
	p = {}
	q = {}
	p[0] = 0
	p[1] = 1
	i = 0
	while(x):
		a,b = divmod(n,x)
		q[i] = a
		if(i>=2): 
			p[i] = (p[i-2] - p[i-1]*q[i-2]) % on
		i+=1
		n,x = x,b
		
	p[i] = (p[i-2] - p[i-1]*q[i-2]) % on

	return (p[i], int((r - p[i]*ox)/on))

print(min(extended_gcd(26513,32321)))
