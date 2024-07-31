#find the min element
list1=list(map(int,input("enter the list:").split(",")))
min1=list1[0]
for i in range(len(list1)):
    if min1>list1[i]:
        min1=list1[i]
print(min1)