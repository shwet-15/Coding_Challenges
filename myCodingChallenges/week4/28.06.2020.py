#Given an integer number n, return the difference between the product of its digits and the sum of its digits.

def subtractProductAndSum(n):
    product=1
    s=0
    while(n>=1):
        n_rem=n%10
        product=product*n_rem
        s=s + n_rem
        n=n//10
    r=product-s
    return r
print(subtractProductAndSum(234))