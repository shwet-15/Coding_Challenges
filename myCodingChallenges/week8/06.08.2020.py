#Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.Find all the elements that appear twice in this array.

def findDuplicates(nums):
    nums.sort()
    i=0
    n=[]
    while(i<len(nums)-1):
        if nums[i]!=nums[i+1]:
             i=i+1
        else:
            n.append(nums[i])
            i=i+2
    return(n)   
print(findDuplicates([4,3,2,7,8,2,3,1]
))    
