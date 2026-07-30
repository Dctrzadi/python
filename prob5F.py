#Create an empty dictionary. Allow $ friends to enter thier favourite language as value and use key as their names. Assume that the names are unique 
s={}
for i in range(4):
    name=input("Enter your name:-")
    lang=input("Enter your lang:-")

s.update({name:lang})
print(s)
