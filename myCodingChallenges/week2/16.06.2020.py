#Given a 32-bit signed integer, reverse digits of an integer.

def reverse(x):
  p=2**31
  a=str(x)
  a=a[::-1]
  if "-" in a:
    z= -int(a[:-1])
  else: 
    z=int(a)
  if z>p-1 or z<-p:
    return 0
  return z  
print(reverse(-4567900))        
       