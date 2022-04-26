# Dictionary = A changeable, unordered collection of unique key: value pairs
#              Fast because they use hashing, allow us to access a value quickly

capitals = {'USA':'Washington DC', 
            'India':'New Dehli', 
            'China':'Beijing',
            'Russia':'Moscow'} 

capitals.update({'Germany':'Berlin'}) # crea una nueva llave y un nuevo valor
capitals.update({'USA':'Las Vegas'}) # Remplaza el valor en la llave de usa
capitals.pop('China') # elimina llaves
# capitals.clear() limpia las llaves de capitals 

print(capitals['Russia'])
print(capitals.get('USA')) # Es lo mismo que el de arriba
print (capitals.keys()) # Imprime todas las llaves
print(capitals.values()) # solo saca los valores 
print(capitals.items()) # Imprime todo el diccionario

for key,value in capitals.items(): # imprime los valores en orden 
    print(key, value)
