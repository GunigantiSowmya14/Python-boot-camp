#remove all  braces from algibric expression
inp=input("")
ans=""
for i in inp:
    if (ord(i)==40 or ord(i)==41 or ord(i)==91 or ord(i)==93 or ord(i)==123 or ord(i)==125 ):
        pass
    else:
        print(i,end="  ")


