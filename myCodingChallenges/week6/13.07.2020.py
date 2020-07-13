
#Students are asked to stand in non-decreasing order of heights for an annual photo.
#Return the minimum number of students that must move in order for all students to be standing in non-decreasing order of height.
#Notice that when a group of students is selected they can reorder in any possible way between themselves and the non selected students remain on their seats.

def heightChecker(heights):
  new_h=sorted(heights)
  count=0
  for i in range(len(heights)):
    if heights[i]!=new_h[i]:
        count=count+1  
  return(count) 
print(heightChecker([1,1,4,2,1,3]))
print(heightChecker([5,1,2,3,4]))

        

      
  
      
