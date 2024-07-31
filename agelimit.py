#age limit for eligibility
name=input("enter your name:")
age=int(input('enter your age:'))
if (age>=18):
    print(f"your{name} you are elgible")
else:
    print(f"your{name} you are not elgible")

#age limit for vehicles
age=60
if(age<=18 or age>24):
    print("only for 2 wheeler")
elif(age==24 or age>45):
    print("two and four wheeler")
else:
    print("all")