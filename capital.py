#to print all the capital letters in a string
n=input("")
ans=" "
for i in n:
    if(ord(i)>=65 and ord(i)<=90):
        ans+=i
print(ans)