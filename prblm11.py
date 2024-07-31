#find the max element  given in a list
list1=list(map(int,input("enter the list:").split(",")))
max1=0
for i in range(len(list1)):
    if max1<list1[i]:
        max1=list1[i]
print(max1)
