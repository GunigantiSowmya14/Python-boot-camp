#loop for a string
#list=list(map(str,input().split(" ")))
s="hello world"
for i in range(len(s)):
    print(s[i],end=" ")


#method 2
for i in s:
    print(i,end="")
