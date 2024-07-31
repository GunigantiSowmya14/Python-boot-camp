#print the sum of numbers in a string
n=input("")
sum=0
for i in n:
    if(ord(i)>=48 and ord(i)<=57):
        sum+=n[i]
print("input value")

