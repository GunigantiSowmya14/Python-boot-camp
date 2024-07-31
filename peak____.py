# to find the peak value****
n=list(map(int,input().split(",")))
for i in range(len(n)):
   if (n[i]>n[i-1] and[i+1]):
      print(n[i],end=" ")
# 87 3 4 5 6 7 14
# 0  1 2 3 4 5 6
#another method
n1=list(map(int,input().split(",")))
count=0
for i in range(1,len(n),-1):
   if(n[i]>n[i-1] and n[i]>n[i+1]):
      count=i
      print(count[i])

#last value
n=list(map(int,input().split(",")))
count=0
for i in range (1,len(n),-1):
      if (n[-1]>n[-1] and n[-2]> count ):
            count=len(n)-1
print(n[count])

