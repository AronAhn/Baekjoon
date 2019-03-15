a = input()
res = [0]*26
for i in a:
    res[ord(i)-97] += 1
for i in res: print(i, end=" ")