#Given an array nums and a value val, remove all instances of that value in-place and return the new length.
#Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#The order of elements can be changed. It doesn't matter what you leave beyond the new length.
def removeElement(nums,val):
    nums.sort()
    i=0
    while(i<len(nums)):
      if(nums[i]==val):
        nums.pop(i)
      else:
        i=i+1  
    return len(nums)       
print(removeElement([3,2,2,3],3))
print(removeElement([0,1,2,2,3,0,4,2],2))