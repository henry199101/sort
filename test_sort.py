#from bubble_sort import bubble_sort, bubble_sort_better
from insert_sort import insert_sort


def test_sort():
	nums0 = []
	nums1 = [1]
	nums2 = [3,1,4,5,7,2,6]
	nums3 = [7,6,5,4,3,2,1]
	for sort in (insert_sort,):
	#for sort in (bubble_sort, bubble_sort_better, insert_sort):
	#for sort in (merge_sort,):
		assert sort(nums0) == []
		assert sort(nums1) == [1]
		assert sort(nums2) == [1,2,3,4,5,6,7]
		assert sort(nums3) == [1,2,3,4,5,6,7]

	print("All testcases pass!")

if __name__ == "__main__":
	test_sort()