#Given an array nums of integers, return how many of them contain an even number of digits.

def findNumbers(nums):
  count=0
  for i in nums:
         n=str(i)
         if len(n) %2==0:
            count+=1
  return(count)  
print(findNumbers(nums = [12,345,2,6,7896] ))    

        