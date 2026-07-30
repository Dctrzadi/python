#Write a program to find out whether a student has passed or failed if it requires a total of 40%
#and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user
sub1=int(input("Enter marks of 1st subject:-"))
sub2=int(input("Enter marks of 2nd subject:-"))
sub3=int(input("Enter marks of 3rd subject:-"))
marks=sub1+sub2+sub3
per=marks/300*100
if(per<40 or sub1/100*100<33 or sub2/100*100<33 or sub3/100*100<33):
    print("FAIL")
else:
    print("PASS")