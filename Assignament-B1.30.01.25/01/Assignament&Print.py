#Assignador con operador "="
x = 5
y = 7
mess1 = "hola mundo"
mess2 = "la operación matematica se realizó con exito"
#puedes ejecutar/run python
print(mess1,"la suma de x+y es igual a: ",x+y,"...",mess2)
print(mess1,"la suma de x+y es igual a: ",x+y)

#puedes ejecutar/run python
# Usando f-strings (forma más moderna y legible):
print(f"{mess1} la suma de x+y es igual a: {x+y}... {mess2}")
print(f"{mess1} la suma de x+y es igual a: {x+y}")

# Otras formas alternativas de hacerlo:
# Usando .format():
print("{} la suma de x+y es igual a: {}... {}".format(mess1, x+y, mess2))

#Usando %:
print("%s la suma de x+y es igual a: %d... %s" % (mess1, x+y, mess2))