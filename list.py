# list = used to store mulltiple items in a single variable

food = ["pizza", "hamburger", "hot dog", "spaghetti"]
food[0] = "sushi" # cambia el elemnto 0 por sushi

food.append("ice cream") # para agregar un valor a la lista
food.remove("hog dog") # elimina el valor 
food. pop() # elimina el ultimo elemento
food.insert(0, "cake") # cambia el elemnto selecionado por el elemnto escrito
food.sort() # sortea elementos dentro de la lista
food.clear()# limpia la la lista



print(food[3]) # inprime el numero de la lista que escribes

for x in food:
    print(x) # sirve para imprimir toda la lista
