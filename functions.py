message="Hello world"
print(len(message))
print(message[8])
print(message[0:5])
print(message[6:11])
print(message[6:])
print(message[:5])
print(message.lower())
print(message.count('l'))
print(message.find('world'))
print(message.replace('world','everyone'))
greeting="Hello"
name="Aditya"
final=greeting+" "+name # here we used the + operator to concatenate two strings 
#also we use "" to add space between two strings
newline= "{},{}".format(greeting,name) # here we used the format method to concatenate two strings
direct=f"{greeting},{name}"# here we used the f-string method to concatenate two strings
bi=f"{greeting},{name.upper()}" # here we used the f-string method to concatenate two strings and also used the upper method to convert the name to uppercase
print(final)
print(newline)
print(direct) 
print(bi)
print(help(str)) # here we used the help method to get the documentation of the str class