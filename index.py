# index operator [] = gives access to a sequence element (str, list, tuples)

name = "luis Cota !"

if(name[0].islower()):
    name = name.capitalize()
print(name)

print(name[:4].upper())
print(name[4:].lower())
print(name[-1])
