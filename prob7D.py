#Write a program to find wheter a given number is prime or not.
num=int(input("Enter number here:-"))
for i in range(2,num):
    if(num%i==0):
        print("not prime")
        break
else:
    print("prime")