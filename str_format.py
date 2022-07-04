# str.format() = optional method that gives users
#                more control when displaying output

from unicodedata import name


animal = "cow"
item = "moon"

print("The " + animal + " jumped over the " + item)#normal
print("The {} jumped over the {}".format(animal, item))# str.format
print("The {1} jumped over the {0}".format(animal, item)) #pistional argument
print("The {animal} jumped over the {animal}".format(animal = "cow",item = "moon"))#keyword argument
text = "The {} jumped over the {}"
print(text.format(animal, item))



name = "Luis Cota"

print("Hello, my name is {}".format(name))
print("Hello, my name is {:20}. Nice to meet you".format(name))#se recorren 10 lugares despues del nombre
print("Hello, my name is {:<20}. Nice to meet you".format(name))#se recorren 10 lugares despues del nombre
print("Hello, my name is {:>20}. Nice to meet you".format(name))#se recorren 10 lugares despues del nombre
print("Hello, my name is {:^20}. Nice to meet you".format(name))#se recorren 10 lugares despues del nombre



number = 3.14159
number1 = 1000

print("The number pi is {:.3f}".format(number))# el 3f saca los tres decimales y los redondea, si es 4 aumenta a 4 decimales.
print("The numberS is {:,}".format(number1))# imprime el numero como tal
print("The numberS is {:b}".format(number1))# imprime number en binario
print("The numberS is {:o}".format(number1))# imprime en hexadecimal
