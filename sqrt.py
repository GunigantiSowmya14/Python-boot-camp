#finding the squarerroot
n1=int(input("enter the value:"))
sum=0
while n1>0:
    value=n1%10
    sum=sum+value**2
    n1=n1//10
print(sum)