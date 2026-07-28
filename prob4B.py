#Write to accept marks of 6 stuents and display them in sorted manner.
marks=[]
n=int(input('Number of marks u want:-'))
for i in range (n):
    mark=int(input("Enter marks:-"))
    marks.append(mark)
    marks.sort()
print(marks)