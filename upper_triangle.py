#print upper triangular matrix
i=0
j=0
for i in range(5):
    for j in range(5):
            if  i==j or i>j:
               print(" ",end=" ")
            else:
                 print("*",end=" ")
    print()