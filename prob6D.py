#write a program to find wheter a given username conatins less than 10 characters or not.
username=input("Enter the username here:-")
print(len(username))
if (len(username)<10):
    print("Less")
else:
    print("Long")