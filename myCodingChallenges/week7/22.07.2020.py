#A peak element is an element that is greater than its neighbors.
#Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
#The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.


def findPeakElement(nums):
    peak=0
    for i in range(1,len(nums)-1):
        if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
            peak=i
    if peak==0:      
        peak= nums.index(max(nums))
    return peak   
print(findPeakElement([1,2,1,3,5,6,4])) 