a=int(input("Enter your age:- "))
if(a>=18):
     print("You are able to use the website")
elif(a<0):
     print("You are entering a worng age")
#elif set of code is executed when "If" conditon is wrong; Its a like a path between if and else
#there can be multiple elif in a condition statements.
elif(a==0):
     print("Your are just born")
else:
     print("Sorry! You can't use the wesbite")
     