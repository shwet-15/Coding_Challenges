#Given two binary strings, return their sum (also a binary string).
#The input strings are both non-empty and contains only characters 1 or 0.

def addBinary(a,b):
  num1=int(a,2)
  num2=int(b,2)
  sum=num1+num2
  return bin(sum).replace("0b","")
print(addBinary("1010","1011"))  