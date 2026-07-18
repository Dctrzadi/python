#tuples are immutable data structures in python which means we cannot change the values of a tuple once it is created. 
tuple_1=(1, 2, 3, 4, 5)
tuple_2=tuple_1
print(tuple_1,tuple_2)
tuple_1[0]=10#This will give an error because we cannot change the values of a tuple once it is created.
