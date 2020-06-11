# Find missing element from range of numbers with n-1 integers
l=[5,9,1,6,2,4,8,3]
l.sort()
j=l[0]
for i in range(len(l)):
  if j==l[i]:
    j=j+1
    continue
else:
  print(j)    
