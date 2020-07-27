#Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.


def findKthLargest(nums,k):
    nums.sort(reverse=True)
    return nums[k-1]
print(findKthLargest([3,2,3,1,2,4,5,5,6],4))    