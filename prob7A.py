#Write a program to print multiplication table of a given number using for loop.
num = int(input("Enter the number whose table you want "))
for i in range(1,11):
    print((num),"X",(i),"=",num*i)
