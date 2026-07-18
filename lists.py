courses=["Python","Java","C++","JavaScript"]
print(courses)
print(len(courses))
print(courses[0])
print(courses[1])
print(courses[2])
print(courses[3])
print(courses[-1])
print(courses[-2])
print(courses[-3])
print(courses[-4])
courses.append("C#")# Append is used to addan item to the end of the list
print(courses)
courses.insert(1,"PHP")# Insert is used to add an item at a specific index
print(courses)
courses2 = "Ruby","Swift"
courses.insert(2,courses2)
courses.extend(courses2)# Extend is used to add multiple items to the end of the list
print(courses)
courses.remove(courses2)# Remove is used to remove an item from the list
print(courses)
courses.pop(3)# Pop is used to remove the last item from the list
popped=courses.pop(3)
print(popped)# Pop is used to remove an item at a specific index
print(courses)
courses.reverse()
print(courses)
courses.sort()# Sort is used to sort the list in ascending order
print(courses)
num=[5,7,8,3,1]
print(num)
num.sort()# Sort is used to sort the list in ascending order
print(num) 
num.reverse()# Reverse is used to reverse the list
print(num)
#else
num.sort(reverse=True)# Sort is used to sort the list in descending order
print(num)
sorted_num=sorted(num)# Sorted is used to sort the list in ascending order
print(sorted_num)
sorted_num=sorted(num, reverse=True)
print(sorted_num)
print(min(num))# Min is used to get the minimum value from the list
print(max(num))# Max is used to get the maximum value from the list
print(sum(num))# Sum is used to get the sum of all the values in the list
print(courses.index("Java"))# Index is used to get the index of a specific value in the list
print("Python" in courses)# In is used to check if a specific value is in the list
for course in courses:# For loop is used to iterate through the list
    print(course)
for  index,course in enumerate(courses):# Enumerate is used to get the index and value of a specific value in the list
    print(index, course)
for index,course in enumerate(courses, start=1):# Enumerate is used to get the index and value of a specific value in the list and also we can specify the starting index
    print(index, course)
courses_str=", ".join(courses)# Join is used to join the list into a string
print(courses_str)