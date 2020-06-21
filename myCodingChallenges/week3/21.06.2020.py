#Given an array of integers, find if the array contains any duplicates.
#Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

def containsDuplicate(nums):
    nums.sort()
    i=0
    j=1
    while(j<len(nums)):
        if(nums[i]==nums[j]):
            return True
        else:
             i+=1
             j+=1
    return False
print(containsDuplicate([2,4,18,22,22]))
print(containsDuplicate([1,5,3,7,1]))
print(containsDuplicate([3,4,5]))    
