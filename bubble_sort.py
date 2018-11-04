def bubble_sort(nums):

	for i in range(len(nums)-1):
		for j in range(0, len(nums)-i-1):
			if nums[j] > nums[j+1]:
				nums[j], nums[j+1] = nums[j+1], nums[j]

	return nums


def bubble_sort_better(nums):

	for i in range(len(nums)-1):
		
		flag = False
		# flag 用于标记内层循环中，是否发生了交换。		
		for j in range(0, len(nums)-i-1):
			if nums[j] > nums[j+1]:
				nums[j], nums[j+1] = nums[j+1], nums[j]
				flag = True	# 发生了交换。

		if flag==False:	break
		# 若未发生交换，则说明数列初始状态是从小到大排列的，即有序的。

	return nums