year=int(input("enter the value:"))
for i in range (2000,2025):
 if(year%400==0 or (year%4==0 and year!=100)):
         print("leap year")
         break
 else:
          print("not a leap year")