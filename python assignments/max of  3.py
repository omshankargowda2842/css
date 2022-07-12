#maximum of 3 values
a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
c=int(input("enter 3rd number:"))
max=a if a<b and a<c else b if b<c else c
print(max)