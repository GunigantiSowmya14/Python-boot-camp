#number of vowels in a string
n=input("enter the string:")
count=0
vowel="aeiou"
for i in n:
    if i in vowel :
            count+=1
print(count)


