import sys
r = sys.stdin.readline
n = int(r().strip())


for _ in range(n):
	m = int(r().strip())
	#if m == 0: 
#		print(0)
#		continue
	dic = {}
	
	for _ in range(int(m)):
		item, part = r().strip().split()
		if part in dic:
			dic[part] += 1
		else: dic[part] = 2
	res = 1
	for v in dic.values():
		res *= v
	print(res-1)