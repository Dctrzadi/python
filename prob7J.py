#Write a program to print multiplication table of n using for loops in reverse order 
n=int(input("enter the number:-"))
for i in range(10,0,-1):
    print((n),"X",(i),"=",n*i)