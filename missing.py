#find the missing number in a array
list1=list(map(int,input("enter the list:").split(",")))
n=10
total=n*(n+1)//2
sum=0
for i in range(len(list1)):
     sum=sum+list1[i]
print(total-sum)