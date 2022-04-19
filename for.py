#for loop = Astatement that will execute it's block of code a
#           a limited amount of times
#           while loop = unlimited 
#           for loop = limited

import time

for i in range(10): #hace un contador del y al 10
    print(i + 1)# al final agrega un numero al contador

for i in range(50, 100 + 1): #agrega un numero al final como arriba en el print
    print(i)

for i in "Luis Cota":
    print(i)

for seconds in range(10, 0, -1):#hace una cuenta regresiva con el -1
    print("seconds")
    time.sleep(1)#hace una pausa de 1 segundo
print("Happy New Year! ")