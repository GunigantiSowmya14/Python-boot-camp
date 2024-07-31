#print the unique characters in a string
n=input("enter the string")
unique=""
count=0
for i in n:
     if  n not in unique:
      unique+=i
print(unique)

