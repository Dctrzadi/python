a=[1,2,3]
b=[1,2,3]
print(id(a))
print(id(b))
print(a == b)
print(a is b) #is operator doesnt only look for values it looks for ids as well
b=a
print(id(a))
print(id(b))
print(a == b)
print(a is b)

#Flase values:
"""
False
None
Zero of any numeric type
Any empty sequence. For example, '',(),[],
Any empty mapping.For example,{}.
Also 0 gives False
"""
condition = -1
if condition:
    print('Evaluated to True')
else:
    print("Evaluated to False")


