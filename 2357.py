import sys
r = sys.stdin.readline

n, m = map(int, r().split())

nums = [int(r()) for _ in range(n)]
k = len(nums)*0.1

order_idx = sorted(range(len(nums)),key=lambda x:nums[x],reverse=True)

# print(nums)
# print(order_idx)

for _ in range(m):
	a, b = map(int, r().split())
	a -= 1
	b -= 1
	#for big scales
	if (b-a > k):
		for i in order_idx:
			if a <= i <= b: break
		target_max = nums[i]
		for i in reversed(order_idx):
			if a <= i <= b: break
		target_min = nums[i]
	else: 
		target = nums[a:b+1]
		target_min = min(target)
		target_max = max(target)
	print(target_min, target_max)