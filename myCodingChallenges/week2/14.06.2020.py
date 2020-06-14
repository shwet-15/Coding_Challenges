def plusOne(digits):
    digits=[str(i) for i in digits]
    digits=''.join(digits)
    digits=int(digits)+ 1
    digits=[int(j) for j in str(digits)]
    return digits
print(plusOne([9,9,9]))
print(plusOne([2,7,9,0]))