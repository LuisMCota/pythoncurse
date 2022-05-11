# keywords arguments = arguments preceded by an identifier when we pass them to a function
#                      The order of the arguments doesnt matter, unlike positional arguments
#                      Python knows the names of the arguments that our function

def hello(first, middle, last):
    print("Hello "+first+" "+middle+" "+last)

hello("Luis Fernando", "Monterrubio", "Cota") # aqui el orden si importa

hello(middle = "Monterrubio", first = "Luis Fernando", last = "Cota")
# aqui el orden no importa porque pusimos las palabras cleve
