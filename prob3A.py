#write a python program to dispaly a user entered name followed by Good Afternoon using input() function.
name= input("please enter your name:-")
print("Good Afternoon {}".format(name))
#using f strings:- this is used to take variable within "{}"
print(f"Good Afternoon {name}")
print("Good Afternoon"+" "+ name)