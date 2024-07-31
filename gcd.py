#gcd
a=int(input("enter value1:"))
b=int(input("enter value2:"))
while b!=0:
    a,b=b,a%b
print("gcd of 2 numbers:",a)
   