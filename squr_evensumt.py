#square evensum
n=int(input("enter the value"))
sum=0
while n>0:
    value=n%10
    if value%2==0:
        sum=sum+value
    n=n//10
print(sum)
