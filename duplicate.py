#find ythe duolicates in array
list1=list(map(int,input("enter the value").split(",")))
duplicate=[]
for i in list1:
    if(i   not in duplicate):
        duplicate.append(i)
print(duplicate)
