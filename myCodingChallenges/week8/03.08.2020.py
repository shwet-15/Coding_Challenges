#Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

def isPalindrome(s):
    n=''
    for i in s:
        if i.isalnum():
             n=n+i
    n=n.lower()
    new_n=''
    for i in range(len(n)-1,-1,-1):
         new_n=new_n + n[i]
    if n==new_n:
            return(True)
    else:
            return(False)
print(isPalindrome("A man, a plan, a canal: Panama"))     
print(isPalindrome("race a car"))              
