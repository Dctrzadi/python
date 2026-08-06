#to use or introduce a function we use "def" keywrod refers to define 
sum = 0

def avg():#this is defining the stucture and code of the fucntion 
    global sum

    for i in range(4):
        num = int(input("Enter Numbers: "))
        sum = sum + num

    average = sum / 4
    print("Average =", average)

avg()#now as we have created the func will now call the func so it performs its tasks 
