import sys
r = sys.stdin.readline

k = int(r())
res = []
for _ in range(k):
    n = int(r())
    if n!= 0: res.append(n)
    else: res.pop()


print(sum(res))