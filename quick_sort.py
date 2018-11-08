from swap import swap


def partition(nums, left, right):
	middle = (left+right) // 2
	pivot = nums[middle]

	swap(nums, middle, right)
	# 现在主元 pivot 等于 nums[right]

	boundary = left
	for index in range(left, right):
		if nums[index] < pivot:
			swap(nums, index, boundary)
			boundary += 1

	swap(nums, boundary, right)

	return boundary


def qsort(nums, left, right):
	if left < right:
		pivotIndex = partition(nums, left, right)
		qsort(nums, left, pivotIndex-1)
		qsort(nums, pivotIndex+1, right)


def quick_sort(nums):
	qsort(nums, 0, len(nums)-1)
