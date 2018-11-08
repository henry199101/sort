from swap import swap

def bubble_sort(nums):
	n = len(nums)

	for i in range(n-1):
		j = 1
		while j <= n-i-1:
			if nums[j-1] > nums[j]:
				swap(nums, j-1, j)
			j += 1


def bubble_sort_better(nums):
	n = len(nums)

	for i in range(n-1):
		
		flag = False
		# flag 用于标记内层循环中，是否发生了交换。		
		j = 1
		while j <= n-i-1:
			if nums[j-1] > nums[j]:
				swap(nums, j-1, j)
				flag = True	# 发生了交换。
			j += 1

		if flag==False:	break
		# 若未发生交换，则说明数列初始状态是从小到大排列的，即有序的。
