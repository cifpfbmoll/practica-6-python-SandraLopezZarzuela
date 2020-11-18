mini = int (input("Escribe un numero para dar valor al minimo"))
maxi = int (input("Escribe un numero para dar el valor maximo"))
list = []

while maxi<mini:
        maxi = int (input("ESCRIBE UN NUMERO MAYOR QUE EL MINIMO!!"))

while maxi>mini:

    inter = int (input ("Escribe un numero intermedio"))
    
    if inter<maxi and inter>mini:
        list.append(inter)
    else:
        print ("Los numeros que hay entre",maxi,"y",mini,"son",list)

