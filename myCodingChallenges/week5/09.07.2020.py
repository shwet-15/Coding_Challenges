#Given a positive integer num consisting only of digits 6 and 9.
#Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

def maximum69Number (num) :
    n=list(str((num)))
    l=[]
    for i in range(len(n)):
        if n[i]=="9":
            n[i]="6"
            new_num1=int("".join(n))
            l.append(new_num1)
            n[i]="9"

        elif n[i]=="6":
            n[i]="9"
            new_num2=int("".join(n))
            l.append(new_num2) 
            n[i]="6"
    if max(l)>num:
            return max(l)
    else:
            return num
print(maximum69Number (6996))           
print(maximum69Number (9999))           