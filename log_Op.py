#logical operators (and, or) = used to check if two or more conditional statements
temp = int(input("What is the temperature outside? "))

if temp >= 0 and temp <= 30: #tambien existe el if not y el elif not
    print("The temperature is good today!")
    print("Go outside!")
elif temp < 0 or temp > 30:
    print("The temperature is bad today!")
    print("Stay inside!")