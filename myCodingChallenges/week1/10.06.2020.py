# Remove duplicates from sorted list and return length of array with no duplicates
def removeDuplicates(nums):
   i=0
   while i<len(nums): 
       if(i==len(nums)-1):
           break
       if(nums[i])==nums[i+1]:
          nums.pop(i+1)
       else:
          i+=1
   return len(nums)       
l=[0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(l))
