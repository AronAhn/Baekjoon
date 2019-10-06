n = int(input())
words = [input() for _ in range(n)]
[print(i) for i in sorted(set(words), key=lambda e: (len(e), e))]