#Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

def toLowerCase(str):
    s_new=''
    for i in str:
        if ord(i)>=65 and ord(i)<=90:
             s_new=s_new + chr(ord(i)+32)
        else:
             s_new=s_new+i  
    return(s_new)
print(toLowerCase("LOVELY"))
print(toLowerCase("HEll0@"))   
print(toLowerCase("GoogleeeeEEEE"))                         