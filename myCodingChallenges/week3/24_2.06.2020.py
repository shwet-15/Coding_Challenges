#Given an integer n and an integer start.Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.
#Return the bitwise XOR of all elements of nums.

def xorOperation(start,n):
    nums=[start+2*i for i in range(n) ]
    e=0
    for i in nums:
         e=e^i
    return e 
print(xorOperation(n = 4, start = 3))  
print(xorOperation(n = 1, start = 7)) 
print(xorOperation(n = 10, start = 5))  

        