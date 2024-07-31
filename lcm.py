#lcm
a=int(input("enter value1:"))
b=int(input("enter value2:"))
n1=a
n2=b
lcm=0
while b!=0:
    a,b=b,a%b
lcm=(n1*n2)/a
print("enter the lcm of 2 numbers:",lcm)
 