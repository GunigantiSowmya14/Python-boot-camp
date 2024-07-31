#your given with a comma seperated natural numbers 1 to 10.print even numbers
list1=list(map(int,input().split(",")))
for i in range(1,len(list1),2):
    if list1[i]%2==0:
       print(list1[i])

#count the number of even numbers
list2=list(map(int,input().split(" ")))
even=0
for i in range(0,len(list2)):
    if list2[i]%2==0:
        even+=1
print(even)

#your give with a space seperated integer list find number of even elements and ood elents in a given list
list3=list(map(int,input().split(" ")))
even=0
odd=0
for i in range(0,len(list3)):
    if list3[i]%2==0:
        even+=1
    else:
         odd+=1
print(even)
print(odd)