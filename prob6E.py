#write a program to find out wheter a given name is present in a list or not.
name=["satyam",'kunal','shivam']
print(name)
check=input("Enter the name you wan tot check:-")
if((check) in (name)):#we used "in" here which is membership operator.
    print("found")
else:
    print("not found")