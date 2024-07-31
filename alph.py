#inputABC,4  opEFG
str1=input("enter the string:")
n=int(input("enter skip values:"))
inp=str1.upper()
empty=""
for i in inp:
    if (i>=97 and i<=122):
        empty+=chr(ord(i)+n)
print(empty)
#xyz
'''n=input("")
count=0
for i in n:
    if (chr('x'),chr('y'),chr('z')):
        count+=1
print(count)'''
