from sympy.ntheory import discrete_log
alice = {"p": "0xde26ab651b92a129", "g": "0x2", "A": "0x52ba1f04804509da"}
bob = {"B": "0x7dd6a241cab0c94e"}
flag = {"iv": "5526838dc2ba63572c9ea3c831d335a8", "encrypted_flag": "6a7fd2604b7e67967b64f212689db6e9a6492ab6bc7fbf73b555ec244efcad11"}
p = int(alice["p"],16)
g = int(alice["g"],16)
A = int(alice["A"],16)
B = int(bob["B"],16)
a = discrete_log(p,A,g)
print(a)
shared_secret = pow(B,a,p)