#taking user input and chossing the requrired value as :1 for append
list1=list(map(int,input().split(" ")))
choice=list1[0]
if (choice==1):
    list1.append(46)
    print(list1)
elif (choice==2):
    list1.pop(2)
    print(list1)
elif (choice==3):
      list1.sort()
      print(list1)
elif (choice==4):
     print(len(list1))