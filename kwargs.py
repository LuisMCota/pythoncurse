# kwargs = parameter that will pack all arguments into a directionary
#          useful so that a funtion can accept a varying amount of keyword argument
#le puedes dar el nombre que quieras a los kwargs (names)


def hello(**names): #kwars te deja usar muchos argumentos en tu funcion
    #print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello", end=" ")# el end sirve para que imprima todo mi nombre en la misma linea
    for key, value in names.items():#sirve para correr todo los elementos que hay en kwargs
        print(value, end=" ")#imprime todos los elementos de kwars

print(hello(first="Luis", middle = "Fernando", last="Monterrubio Cota"))