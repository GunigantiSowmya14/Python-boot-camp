#input=hello.......word   op=------helloword
n=input()
count=0
ans=""
for i in n:
    if(i=="-"):
        count+=1
    else:
        ans=ans+i
print("-"*count+ans)
