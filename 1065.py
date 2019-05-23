n = int(input())
if n < 100: print(n)
else:
    res = 0
    for n in range(100, min(n+1,1000)):
        n1, n2, n3 = map(int, str(n))
        if n1 - n2 == n2 - n3: res += 1
    print(res+99)
