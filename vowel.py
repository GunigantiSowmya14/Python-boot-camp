list1=list(map(str,input("enter the string").split(" ")))
vowel='a,e,i,o,u'
count=0
for i in list1:
    if(i==vowel):
        count+=1
        break
        print(vowel[i])