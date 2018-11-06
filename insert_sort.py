def insert_sort(nums):
	for i in range(1, len(nums)):
		itemToInsert = nums[i]
		j = i
		while j>=1 and itemToInsert<nums[j-1]:
			nums[j] = nums[j-1]
			j -= 1
		nums[j] = itemToInsert
