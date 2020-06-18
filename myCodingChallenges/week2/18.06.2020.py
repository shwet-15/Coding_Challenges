#Determine whether an integer is a palindrome.
#An integer is a palindrome when it reads the same backward as forward.
def isPalindrome(x):
  x=str(x)
  y=x[::-1]
  if "-" in y:
    return False
  else:
    x=int(x)
    y=int(y)
    if(x==y):
      return True
    else:
      return False  
print(isPalindrome(-121))
print(isPalindrome(121))
print(isPalindrome(10))