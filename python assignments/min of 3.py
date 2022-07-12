a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
c=int(input("enter 3rd number:"))
min=a if a>b and a>c else b if b>c else c
print(min)
