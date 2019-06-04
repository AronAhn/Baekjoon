import itertools

nums = []
for _ in range(9):
	nums.append(int(input()))
target = sum(nums) - 100

for i in itertools.combinations(nums, 2):
	if sum(i) == target: break

nums.remove(i[0])
nums.remove(i[1])
for i in nums: print(i)