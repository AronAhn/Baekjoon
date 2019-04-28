import sys
r = sys.stdin.readline

peo = [0]
for i in range(4):
    a, b = map(int, r().split())
    peo.append(peo[i] + (b-a))
print(max(peo))