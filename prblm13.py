#replace the elements in  an array with average of max and min element
list1=list(map(int,input("enter the list:").split(",")))
avg=0
min1=0
max1=0
max1=list1[0]
for i in range(len(list1)):
    if max1<list1[i]:
        max1=list1[i]
min1=list1[0]
for i in range(len(list1)):
    if min1>list1[i]:
        min1=list1[i]
avg=(min1+max1)/2
for i in range(len(list1)):
    list1[i]=avg
print(*list1)
 