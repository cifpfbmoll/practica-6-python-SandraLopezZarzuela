num1 = int (input ("ESCRIBE UN NUMERO"))
num2 = int (input ("ESCRIBE OTRO NUMERO MAYOR QUE EL ANTERIOR"))
while num1>num2:
    if num2>num1:
        print (num2, "no es mayor que", num1)
    num2 = int (input ("VUELVE A INTRODUCIR EL NUMERO"))
print ("Los numeros que has escrito son", num1, "y", num2)