#Write a store 7 fruits in alist entered by the user.
'''fruits=[]
f1=input("Enter Fruits name:-")
fruits.append(f1)
f2=input("Enter Fruits name:-")
fruits.append(f2)
f3=input("Enter Fruits name:-")
fruits.append(f3)
f4=input("Enter Fruits name:-")
fruits.append(f4)
f5=input("Enter Fruits name:-")
fruits.append(f5)
f6=input("Enter Fruits name:-")
fruits.append(f6)
f7=input("Enter Fruits name:-")
fruits.append(f7)
print(fruits)'''

new_fruit=[]
n=int(input("Enetr the number of fruits you want:-"))
for i in range (n):
    add=input("Enter Fruits name:-")
    new_fruit.append(add)
print(new_fruit)