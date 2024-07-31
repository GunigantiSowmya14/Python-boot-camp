#write a program for prime number between a range
n=int(input("enter value:"))
n1=int(input("enter value:"))
for i in range(n,n1+1):
    for j in range(2,i):
        if i%j==0:
          break
    else:
        print(i)
     
