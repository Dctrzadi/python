student ={'name': "John", "age": 20, "grade": "A"}
#in this before ":" are keys and after that there is their value
print(student["name"]) #gets the value of key "name"
print(student.get('lamda')) #gets help in by giving by default value which is "none".
print(student.get('lamda', 'Not Found')) #gets help in by giving by default value which is "Not Found"
student["lambda"] = "Some Value"#it adding new key and value in dictionary
print(student["lambda"])
student.update({"age": 21}) #it updates the value of key "age"
print(student["age"])
del student["grade"] #it deletes the key and value of key "grade"
student.pop("age") #it removes the key and value of key "age" and returns the value of key "age"
print(student)
print(len(student))
print(student.keys())
print(student.values())
print(student.items())
for key in student:
    print(key)
for key,value in student.items():
    print(key,value)