from swap import swap


def select_sort(nums):
	n = len(nums)
	i = 0

	while i <= n-2:

		minIndex = i
		j = i+1

		while j <= n-1:
			if nums[j] < nums[minIndex]:
				minIndex = j

			j += 1

		swap(nums, i, minIndex)

		i +=1


def select_sort_better(nums):
	n = len(nums)
	i = 0

	while i <= n-2:

		minIndex = i
		j = i+1

		while j <= n-1:
			if nums[j] < nums[minIndex]:
				minIndex = j

			j += 1

		if minIndex != i:
			swap(nums, minIndex, i)

		i += 1
