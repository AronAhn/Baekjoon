import sys
r = sys.stdin.readline

n_case = int(r())
cases = [r() for _ in range(n_case)]


for case in cases:
	n_student, *scores = (map(int, case.split(" ")))
	mean_score = sum(scores)/n_student
	above_average = sum(map(lambda x: x>mean_score, scores))
	print("{0:.3f}%".format(round(above_average*100/n_student, 3)))