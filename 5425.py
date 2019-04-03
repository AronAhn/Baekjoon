import sys
r = sys.stdin.readline
n_from, n_to = r().strip().split(" ")
n_from = int(n_from)
n_to = int(n_to)

max_sq = int(n_to**0.5)
squares = [i*i for i in range(2,max_sq+1)]


res = set()
for i in squares:
	if i in res: continue
	res = res | set([j for j in range((int(n_from/i)+1)*i, n_to+1, i)])
	#print(res)



print(n_to - n_from + 1 - len(res))
print(res)