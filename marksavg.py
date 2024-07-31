#findig the marks and avg of 3subjects
name=input("enter your name:")
sub1=int(input("enter your marks 1:"))
sub2=int(input("enter your marks 2:"))
sub3=int(input("enter your marks 3:"))
sum=0
avg=0
sum=sub1+sub2+sub3
avg=sum/3
print(f"hello{name} ,your marks{sum} ,your average{avg}")

#another method
name=(input("enter your name"))
s1=int(input())
s2=int(input())
s3=int(input())
print(f"your marks{s1+s2+s3} avg marks {(s1+s2+s3)/3}")