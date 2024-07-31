n=int(input("enter the value:"))
rev=""
while n>0:
    value=n%10
    rev=rev+str(value)
    n=n//10
ans=int(rev)
print(ans)
print(int(rev))