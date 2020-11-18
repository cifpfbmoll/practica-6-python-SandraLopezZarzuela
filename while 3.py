print ("BIENVENIDO A TU LISTA DE NOTAS")
print ("Si introduces una nota inferior a 0 o superior a 10\nTu lista se finalizara")
notas = int (input ("INTRODUCE TU NOTA: "))
list = []
while notas>0 and notas<10 :
    list.append (notas)
    notas = int (input ("INTRODUCE TU OTRA NOTA: "))
print ("AQUI TIENES TU LISTA DE NOTAS: ", list)