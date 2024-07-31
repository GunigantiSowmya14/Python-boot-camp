year=list(map(int,input().split(",")))
count=0
for i in range (2000,2025):
 if(year[i]%400==0 or (year[i]%4==0 and year[i]!=100)):
        print("leap year")
        break
 else:
          print("not a leap year")