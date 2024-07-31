#print the element in particular index(for many cycles)
k=int(input("enter the value of k:"))
my_list=list(map(int,input().split(",")))
length=len(my_list)
for i in range(len(my_list)):
        #index=k%len(my_list)
        #print(my_list[index])
        print(my_list[k%length]) 
        break

#for one cycle

k=int(input("enter the values of k:"))
my_list1=list(map(int,input("list:").split(",")))
length=len(my_list1)
for i in range(len(my_list1)):
        if length<k:
                print(my_list1[k-length])
        break
else:
        print(my_list1)

