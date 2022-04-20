# loop control statements = Change a loops execution from its normal sequence
# break = used to determine the loop entirely 
# continue = skips to the next iteration of the loop 
# pass = does nothing, acts as a placeholder

while True:
    name = input("Enter your name: ")
    if name != "":#mientras el input este vacio el loop no va a acabar
        break


phone_number = "999-366-6194"
for i in phone_number:
    if i == "-":
        continue
    print(i, end = "")# el end sirve para que no haga saltos de linea
    

for i in range(1, 21):# para quitar un numero
    if i == 13:
        pass
    else: # imprime todo lo demas excepto el 13
        print(i)

