#Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
#Return the answer in an array.

def smallerNumbersThanCurrent(nums):
    l=[]
    for i in range(len(nums)):
        c=0
        for j in range(len(nums)):
            if(nums[i]>nums[j] and i!=j):
                 c=c+1
        l.append(c)
    return l
print(smallerNumbersThanCurrent([8,1,2,2,3])) 
print(smallerNumbersThanCurrent([6,5,4,8])) 
print(smallerNumbersThanCurrent([7,7,7,7])) 