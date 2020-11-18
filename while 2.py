print ("BIENVENIDO A TU LISTA DE NUMEROS\nPARA ACABAR LA LISTA ESCRIBE SALIR")
numero = input ("ESCRIBE UN NUMERO: ")
list = []
while numero != "SALIR":
    list.append(numero)
    numero = input ("ESCRIBE OTRO NUMERO: ")
print ("AQUI ESTA TU LISTA DE NUMEROS: ", list)