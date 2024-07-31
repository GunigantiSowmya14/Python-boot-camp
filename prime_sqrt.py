n=int(input("enter value:"))
a=n**0.5
count=0
if a==1:
    print("not a prime number")
elif a==2:
    print("prime number")
for i in range (2,int(a+1)):
    if n%i==0:
      count+=1
      break;
if (count==0):
    print("prime number")
elif(count>0):
    print(" not a prime number")
else:
    print("not a prime number")
