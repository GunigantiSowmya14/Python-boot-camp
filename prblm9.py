#find the element that is present in k+n index

k=int(input("enter the k value:"))
n=int(input("enter the n value:"))
my_list=list(map(int,input("enter the value of list").split(",")))
length=len(my_list)
if(length<k+n):
    print("error")
else:
    for i in range(len(my_list)):
         print(my_list[k+n])
         break
    
