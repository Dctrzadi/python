n_str = input("Enter the number of rows: ")
n = int(n_str)
for i in range(1, n + 1):
   for j in range(n - i):
    print(' ' * (n - i), end='')
print(' *' * i)