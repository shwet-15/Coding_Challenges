#Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.
#Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.

def findLucky(arr):
   l=[]
   for i in arr:
      if arr.count(i)==i:
          l.append(i)
   l=set(l)  
   l=list(l) 
   l.sort()
   if len(l)==0:
      return -1 
   else:
     return l[-1] 
print(findLucky([1,2,4,1,2]))     
print(findLucky([5,5,5,5,5]))  
print(findLucky([1,2,3,2,1,2]))     


        