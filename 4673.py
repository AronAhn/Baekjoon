g = list(range(10000,0,-1))
while g:
	t = g.pop()
	print(t)
	while t < 10000:
		t = sum([int(i) for i in str(t)])+t
		if t in g: g.remove(t)
		else: break