#Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.
#If the last word does not exist, return 0. 

def lengthOfLastWord(s):
   s=s.strip()
   if(len(s)>=1):
       s=s.split()
       l=s[-1]
       return(len(l))
   else:
       return 0
print(lengthOfLastWord("hello hi"))
print(lengthOfLastWord(""))    
print(lengthOfLastWord("  "))                 