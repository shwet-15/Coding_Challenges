#Convert binary string to decimal
b="1010"
b=[int(i) for i in list(b)]
j=0
sum=0
for i in range(len(b)-1,-1,-1):
  sum=sum + (b[i]*2**j)
  j=j+1
print(sum)  