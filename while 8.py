limite = int (input ("Escribe un numero limite"))
numero1 = int (input("Escribe numeros hasta que su suma de el limite"))

list = [numero1]

while numero1>limite:
    numero1= int (input ("EL NUMERO TIENE QUE SER MAS PEQUEÑO QUE EL LIMITE!!"))

numero2 = int (input("Escribe numeros hasta que su suma de el limite"))

while limite > numero1+numero2 :
    numero2 = int (input("Escribe numeros hasta que su suma de el limite"))
    list.append(numero2)
    numero3 = numero1+numero2
    
    while numero3>limite:
        print ("El numero", numero3, "es demasiado grande escribe otro valor")
        numero2 = int(input("nuevo valor: "))

if limite == numero3:
    print ("El limite a alcanzar es",numero1,"la lista creada es", list)
