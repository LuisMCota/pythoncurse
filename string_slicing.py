# slicing = create a substrating by extracting elements from another string
#indexing[] or slice()
#[star:stop:step]



name = "Luis Fernando Monterrubio Cota"
firstname = name[:13]#selecciona las primeras 13 letras de mi nombre, asi se asumira que empieza en 0 a 13
last_name = name[4:]#selecciona los caracteres apartir del 4
funky_name = name[0:8:2]
reversed_name = name[::-1]

print(firstname)
print(last_name)
print(funky_name)

Website1 = "http://google.com"
Website2 = "http://wikipedia.com"
slice = slice(7, -4)#quita las pimeros 7 caracteres y los ultimos 4 del objeto
print (Website1[slice])
print(Website2[slice])
