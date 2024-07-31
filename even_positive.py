a=int(input("enter the value of a:"))
if(a%2==a or a>=0):
    print("even positive")
elif(a%2==a or a<0):
    print("even negative")
elif(a%2!=a or a>=0):
    print("odd positive")
else:
    print("odd negative")