# set = a collection which is unordered, unindexed. No duplicate values

utensils = {"fork", "spoom", "knife"}
dishes = {"bowl", "plate", "cup"}

utensils.add("napkin") # añade un nuevo elemnto
utensils.remove("fork") # quita un elemnto
utensils.clear() # limpia el set
utensils.update(dishes) # cambia utensils por dishes
dinner_table =  utensils.union(dishes)
print (utensils.difference(dishes)) # que es lo que tienen de diferencia los dos sets

for x in utensils:
    print(x)