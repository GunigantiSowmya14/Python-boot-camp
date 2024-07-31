#given an space seperated integer list ,find the average of elements present in given index
list=list(map(int,input().split(" ")))
total=0
                                     #count=0
length=len(list)
for i in range(len(list)):
    if(list[i]%2==0):
        total+=1
                                       #total+=list[i]
                                          #count+=1

average=total/length
print(average)
                                           #print(total/count)
        