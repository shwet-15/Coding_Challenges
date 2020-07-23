#Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.


def singleNumber(nums):
    nums.sort()
    l=[]
    i=0
    while(i<len(nums)-1):
        if nums[i]==nums[i+1]:
            i=i+2
        else:
            l.append(nums[i])
            i=i+1  
    if len(l)==1:
        l.append(nums[-1])
    return l 
print(singleNumber([2,5,7,5,2,3]))
print(singleNumber([1,5,8,7,1,5]))
        