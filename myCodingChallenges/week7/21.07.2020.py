#Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 
#Return the number of negative numbers in grid.

def countNegatives(grid):
  c=0
  for i in grid:
     for j in i:
        if j <0:
           c=c+1
  return(c)      
print(countNegatives(grid=[[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))