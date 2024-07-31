#append 1 to 100 in a empty list
n=int(input("enter the n value"))
list=[]
for i in range(1,n+1):
    list.append(i)
    print(i,end=" ")