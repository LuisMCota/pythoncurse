# args = parameter that will pack all arguments into a tuple
#        useful so that a function can accept a varying amount of arguments

numbers1 = int(input("Number 1: "))
numbers2 = int(input("Number 2: "))
numbers3 = int(input("Number 3: "))

def add(*args): #se define el tupple
    sum = 0
    for i in args:
        sum += i
    return sum

print (add(numbers1,numbers2, numbers3))#suma todo dentro del add por el for