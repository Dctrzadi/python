#Write a program to find the greatest of four numbers entered by the user.
a=int(input("Enter the 1st numbers here:-"))
b=int(input("Enter the 2nd numbers here:-"))
c=int(input("Enter the 3rd numbers here:-"))
d=int(input("Enter the 4th numbers here:-"))
if(a>b and a>c and a>d):
    print( a,":-A is the greatest number")
elif(b>a and b>c and b>d):
    print(b,":-Bis the greatest number")
elif(c>a and c>b and c>d):
    print(c,":-C is the greatest number")
else:
    print(d,":-D is the greatest number")