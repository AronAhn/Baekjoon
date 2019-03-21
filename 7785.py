import sys
r = sys.stdin.readline

n = r().strip()

res = dict()
for _ in range(int(n)):
    per, stat = r().strip().split(" ")
    res[per] = stat

for i in sorted(res.keys(), reverse=True): 
	if res[i] == "enter": print(i)