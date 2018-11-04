def insert_sort(nums):
	i = 1
	while i <= len(nums)-1:
		itemToInsert = nums[i]
		j = i

		while j >= 1:
			if itemToInsert < nums[j]:
				nums[j] = nums[j-1]
				j -= 1
			else:
				break

		nums[j] = itemToInsert		
		i += 1

	return nums