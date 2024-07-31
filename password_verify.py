#mr.x is trying to create a new password for his instagram account.these are required cond for creating new password
#cond1:min length=8,max len=15
#cond2:only@,/ are allowed in a password
#cond3:no space are allowed
#cond4:only alpha,numerics are allowed
#u r supposed to print if length is exactly 8,length is b/w 8---12 medium  ,length b/w 12----15 strong
name=input(" ")
length=len(name)
count=0
if (length>=8):
    print("follow the conditions")
str="@ /"
for i in name:
     if(i==str[0] or str[1] ):
        count+=1
        break;
     if(i!=""):
         count+=1
         break;
if(length>=8 or length<=12):
    print("medium")
elif(length>=12 or length<=15):
    print("strong")
     

    
