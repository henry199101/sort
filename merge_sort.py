def merge(a, b):
	res = []

	A = 0
	B = 0

	while A<len(a) and B<len(b):
		if a[A] < b[B]:
			res.append(a[A])
			A += 1
		else:
			res.append(b[B])
			B += 1

	if A==len(a):
		res.extend(b[B:])
	if B==len(b):
		res.extend(a[A:])

	return res


def merge_sort(nums):
	if len(nums)<=1:
		return nums

	mid = len(nums)//2
	right_head = mid+1

	return merge(merge_sort(nums[:mid+1]), merge_sort(nums[mid+1:]))


def test_merge():
	a1 = [2, 3]
	b1 = [1, 4]
	a2 = [2, 3, 5]
	b2 = [2, 5]
	assert merge(a1, b1) == [1, 2, 3, 4]
	assert merge(b1, a1) == [1, 2, 3, 4]
	assert merge(a2, b1) == [1, 2, 3, 4, 5]
	assert merge(b1, a2) == [1, 2, 3, 4, 5]
	print("Function " + merge.__name__ + "'s testcases pass!")


if __name__ == "__main__":	
	test_merge()
