# scope = The region  that a variable is recognizaed
#         A variable is only available from inside the region it is created.
#         A global and locally scoped versions of a variable can be created

name = "Luis" # global scope (available inside & outside functions)

def display_name():
    name  = "Cota" # local scope (available only inside this function) 
    print(name) # imprime la variable local

display_name()
print(name) # imprime la variabel global