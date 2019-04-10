import sys
r = sys.stdin.readline

def cal(M):
	if M <= 0: return(0)
	upp_res = []
	nd = len(str(M))
	for d in range(nd):
		upp_tg = int(str(M)[-d-1])
		upp = ((M//(10**(d+1))))*45*(10**d) + sum(range(0,(upp_tg)))*(10**d)
		if d != 0: upp += ((M%(10**d)+1)*upp_tg)
		else: upp += upp_tg
		upp_res.append(upp)
	return(sum(upp_res))

n = r().strip()
for _ in range(int(n)):
	a, b = r().split(" ")
	a = int(a)
	b = int(b)
	print(cal(b) - cal(a-1))
