'''
AND
OR
NOT
'''

user = 'Admin'
logged_in= True


if user== 'Admin' and logged_in==True:
    print('Admin page')
else:
    print('Error') #in "AND" logical operator both values must be true


if user== 'Admin' or logged_in==True:
    print('Admin page')
else:
    print('Error') #in "OR" logical operator any of the values must be ture


if user== 'Admin' or logged_in==True:
    print('Admin page')
else:
    print('Error') #in "OR" logical operator any of the values must be ture

if not logged_in:
    print('Please Log In')
else:
    print('Welcome')#in "NOT" logical operator ture turns false and false turns true

