#Given an array of numbers arr. A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.
#Return true if the array can be rearranged to form an arithmetic progression, otherwise, return false.

def canMakeArithmeticProgression(arr):
   arr.sort()
   diff=abs(arr[0]-arr[1])
   for i in range(1,len(arr)-1):
      d=abs(arr[i]-arr[i+1])
      if d==diff:
        continue
      else:
        return False  
   else:
     return True
print(canMakeArithmeticProgression([1,2,4]))
print(canMakeArithmeticProgression([5,1,3]))

  