#mylist
my_list=[1,2,-3,4]
print(*my_list)

#append:adding the value
my_list.append(99)
print(my_list)

#insert :value to inserted
my_list.insert(8000,7)
print(my_list)

#length :length of the list
print(len(my_list))

#pop :eliminate the last value
my_list.pop(3)

#sum of list
my_list_2=[5,6,-7,8]
new_list=my_list+my_list_2
print(*new_list)

#pop of sum list
new_list.pop()
print(*new_list)

#copy
new_list=my_list.copy()
print(*new_list)

#count
cnt=my_list.count(2)
print(cnt)

#sorting
sort=new_list.sort()
print(new_list)