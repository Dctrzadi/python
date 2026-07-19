import os

# Specify the directory path
path = 'C:/Users/HP/OneDrive/Desktop/Web Tech'

# Print the contents of the directory
contents = os.listdir(path)
for item in contents:
    print(item)