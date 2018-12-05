# coding:utf-8

from swap import swap


"""
将二叉树中的，以 nums[p] 为根的子堆，
调整为最大堆。
（下滤 根节点 nums[p]）

p 是根节点所在的下标；
n 是当前堆一共有多少个元素。
"""
def filter_down(nums, p, n):
	''' 取出根节点存放的值 '''
	rootVal = nums[p]

	parentIdx = p
	while 2*parentIdx+1 <= n-1:
		''' kidIdx 暂时指向左儿子 '''
		kidIdx = 2*parentIdx+1

		''' 左儿子 kidIdx 不等于 n-1，即左儿子不是最后 1 个结点，
		也就是说，还有右儿子 '''
		if kidIdx != n-1 and nums[kidIdx] < nums[kidIdx+1]:
			kidIdx += 1
			''' kidIdx 指向较大的子结点 '''

		''' rootVal 找到了合适的位置 '''
		if rootVal >= nums[kidIdx]:
			break
		''' 如果 rootVal 比子结点小，
		则下滤 rootVal。
		（将较大值往上移动）'''
		else:
			nums[parentIdx] = nums[kidIdx]

		''' 将父节点的指针往下移动 '''
		parentIdx = kidIdx

	nums[parentIdx] = rootVal


def heap_sort(nums):
	n = len(nums)

	''' 建立最大堆 '''
	for index in range(n//2-1, -1, -1):
		filter_down(nums, index, n)

	''' 删除最大堆的顶部的最大项
	将最大堆的最大项与最后 1 项交换位置，
	然后将除最后 1 项的剩余部分，调整为最大堆；
	重复上面的操作。
	'''
	for index in range(n-1, 0, -1):
		swap(nums, 0, index)
		filter_down(nums, 0, index)


def test():
        nums0 = [1,2,3]
        nums1 = [1,3,2]
        nums2 = [2,1,3]
        nums3 = [2,3,1]
        nums4 = [3,1,2]
        nums5 = [3,2,1]
        nums6 = [5,1,6,3,4,8]
        nums7 = [6,1,8,3,4,5]
        for nums in (nums0, nums1, nums2, nums3, nums4, nums5, nums6, nums7):
                filter_down(nums, 0, len(nums))
        assert nums0 == [3,2,1]
        assert nums1 == [3,1,2]
        assert nums2 == [3,1,2]
        assert nums3 == [3,2,1]
        assert nums4 == [3,1,2]
        assert nums5 == [3,2,1]
        assert nums6 == [6,1,8,3,4,5]
        assert nums7 == [8,1,6,3,4,5]

        nums = [7,4,5,3,8,9]
        heap_sort(nums)
        assert nums == [3,4,5,7,8,9]
        print('Pass!')


if __name__ == '__main__':
	test()
