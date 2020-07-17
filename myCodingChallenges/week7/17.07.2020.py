#Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

def sortedSquares(A):
  s=[]
  for i in A:
    s.append(i*i) 
  return sorted(s)
print(sortedSquares([-4,-1,0,3,10])) 
print(sortedSquares([-7,-3,2,3,11])) 
