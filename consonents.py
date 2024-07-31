#print the number  to find consonents
n=input("enter the string:")
count=0
consonents="bcdfghjklmnpqrstvwxyz"
for i in n:
    if i in consonents:
            count+=1
print(count)

