#sets are unordered collections of unique elements in python. 
set_1={1, 2, 3, 4, 5}
print(set_1)
courses={"python", "java", "c++", "javascript"}
print(courses)
#in sets there is no impact on numbers 
#and when there is duplucate elements it only take one of them
print("java" in courses)
tech={"C", "C++", "Java", "Python", "JavaScript"}
print(courses.intersection(tech))#this will give the common elements in both sets
print(courses.union(tech))#this will give all the elements in both sets
print(courses.difference(tech))#this will give the elements which are in courses but not in tech