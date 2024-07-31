#print upper triangular matrix
i=0
j=0
for i in range(5):
    for j in range(5):
            if i>j:
               print(",",end="\t")
            else:
                 print("*",end=" ")
    print()

#print lower triangular matrix
i=0
j=0
for i in range(5):
    for j in range(5):
            if i<j:
               print(",",end="\t")
            else:
                 print("*",end=" ")
    print()


#print rhombus
i=0
j=0
for i in range(10):
    for j in range(10):
            if i>=j:
               print(" ",end="\t")
            else:
                 print("*",end=" ")
    print()


#print*** pallarogram
i=0
j=0
n=0
for i in range(5):
    for j in range(5):
            if n-i==j:
               print(",",end="\t")
            else:
                 print("*",end=" ")
    print()


#print number matrix
