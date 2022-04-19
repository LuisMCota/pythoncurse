#nested loop = The "Ineer loop" will finish all of it's iterations before 
#              finishing one iteration of the "outer loop"

rows = int(input("How many rows? "))
columns = int(input("How many columns? "))
symbol = input("Enter a Symmbolto use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end = "")#se introduce una linea nueva de caracteres debido a que es un print
    print()