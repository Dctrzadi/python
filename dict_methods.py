marks={'Aditya':99, #here aditya is a key and it holds 99 value
'Varun':90,
50:'vijay',
'Vishesh':98,
'Satyam':98}
print(marks.items())#.item()=prints all the items of the dictionary
print(marks.keys())#.keys()=prints all the keys in the dictionary
print(marks.values())#.values()=prints all the values in the dictionary
marks.update({'Vigensh':100,'Aditya':98})#.update({key:value})=helps to update the dictionary
print(marks)
#using .update() you can update the old values of the dictionary and also insert new key-vale set
print(marks.get("Satyam"))
#get helps in getting the value of the key inside (). It prints value of key if available else none gets printed


""" THERE IS A DIFFERENCE BETWEEN .get() & []
.get gives none if the key is not their on the other hand the [] gives you error if the key is not present in the dictionary"""
marks.pop('Varun')#pop() removes the specific items from the dictionary 
print(marks)
marks.popitem()#popitem() removes the last entered key from the dictionary  
print(marks)