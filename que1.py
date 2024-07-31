a=int(input("no of apples:"))
b=int(input("no of bananas:"))
c=int(input('no of oranges:'))
cost_apple=15
cost_banana=4
cost_orange=5
cost=0
cost=(a*cost_apple)+(b*cost_banana)+(c*cost_orange)
if(cost>=700):
    print("cheated")
else:
    print("not cheated")

#even and positive,odd and even
a=int(input("enter the value of a:"))
if(a==a%2 and a>=0):
    print("even and positive")
elif(a==a%2 and a<=0):
    print("even and negative")
elif(a%2|a and a>=0):
    print("odd and positive")
else:
    print("odd and negative")