def insert_sort(nums):
	i = 1
	n = len(nums)

	while i <= n-1:
		j = i
		itemToInsert = nums[i]

		while j >= 1 and itemToInsert < nums[j-1]:

			nums[j] = nums[j-1]
			j -= 1

		nums[j] = itemToInsert

		i += 1
