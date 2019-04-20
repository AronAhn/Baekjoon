import sys
r = sys.stdin.readline


def Binom(n,k):
	C = [[0 for i in range(j)] for j in range(n+1)]
	print(C)
	for i in range(n+1):
		for j in range(min(i,k)):
			if (j==0)|(j==i): C[i][j] = 1
			else: C[i][j] = C[i-1][j-1] + C[i-1][j]
	return C[n][k]

while True:
	n, k = r().strip().split(" ")
	n = int(n)
	k = int(k)
	print(Binom(n,k))
