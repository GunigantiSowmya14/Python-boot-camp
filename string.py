#string: methods in string are *is alpha,*is digit,is algim,
#is upper,is lower,check lower,convert to upper case,tittle case,swap case,
#n=input("enter the string:")
n="divya"
upper=0
lower=0
print(n.upper())
print(n.lower())
print(n.title())
print(n.swapcase()) #lower-upper,upper-lower
print(n.replace('w','u'))# exchangevalues
print(n.split())
print(n.capitalize())
print(n.strip())# remove the spaces
print(n.isalpha()) #bool gives true false
print(n.isalnum())
print(n.isascii())
print(n.isnumeric()) # numbers from 0--9
print(n.isprintable())
print(n.isdecimal())
print(n.islower())
print(n.isupper())
print(n.isdigit())

#ascii
print(ord('A'))
print(chr(65))