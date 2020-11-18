limite = int (input ("Escribe un numero limite"))
numero1 = int (input("Escribe numeros hasta que la suma supere el limite"))
list = [numero1]
while limite>numero1:
    numero2= int (input("Escribe numeros hasta que la suma supere el limite"))
    list.append(numero2)
    numero1 = numero1+numero2
    numero3 = numero1
    if numero3>limite:
        print ("El limite a superar es",limite,"La lista creada es", list, "ya que la suma de estos numeros es",numero3)