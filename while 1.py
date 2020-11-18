print ("Bienvenido a tu lista de palabras\n Para acabar la lista pulsa ENTER")
a= input ("Escribe una palabra: ")
list = []
while a!=" ":
    list.append(a)
    a = input ("Escribe otra palabra: ")
print ("TU LISTA DE PALABRAS ES", list)