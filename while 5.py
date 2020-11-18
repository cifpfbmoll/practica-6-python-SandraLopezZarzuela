numero = int (input ("ESCRIBE NUMEROS"))
otroNumero = int (input("ESCRIBE OTRO NUMERO"))
list = [numero]

while numero<otroNumero:
    numero = otroNumero
    list.append(otroNumero)
    otroNumero = int(input("ESCRIBE OTRO NUMERO"))
print ("LOS NUMEROS QUE HAS ESCRITO SON: ", list)
