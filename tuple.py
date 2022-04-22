# tuple =  collection which is ordered and unchangeable
#          used to group together related data.
 
student = ("Luis", 21, "male")

print(student.count("Luis")) # es un contador
print(student.index("male")) # la pocision en la que se encuentran los valores 

for x in student: # imprime todo el tuple
    print(x)

if "Luis" in student:
    print("Luis is here!")