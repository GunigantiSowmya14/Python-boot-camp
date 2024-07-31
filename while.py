n=123
sum=0
while n>0:
    value=n%10
    sum=sum+value
    n=n//10
print(sum)

#find the sum of square of digit in a given number
n1=int(input(""))
sum=0
while (n>0):
    value=n%10
    sum=sum+value^2
    n=n//10
print(sum)