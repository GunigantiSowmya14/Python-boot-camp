#vowels followed by consonents
n=input("enter the string")
vowels="aeiou"
consonents="bcdfghjklmnpqrstvwxyz"
name=""
for i in n:
    if(i in vowels):
        name+=i
for i in n:
      if(i in consonents):
        name+=i
print(name)

