##Unviersidad del Valle de Guatmemala
##Inteligencia Artificial
##Autor: Michelle Bloomfield Fong 16803

entrada = input("Ingrese los numeros del sudoku:\n")

l1 = entrada[0] +" "+ entrada[1] +" "+ entrada[2] +" "+ entrada[3]
linea1 = l1.split()
l2 = entrada[4] +" "+ entrada[5] +" "+ entrada[6] +" "+ entrada[7]
linea2 = l2.split()
l3 = entrada[8] +" "+ entrada[9] +" "+ entrada[10] +" "+ entrada[11]
linea3 = l3.split()
l4 = entrada[12] +" "+ entrada[13] +" "+ entrada[14] +" "+ entrada[15]
linea4= l4.split()

c1 = entrada[0] +" "+ entrada[1] +" "+ entrada[4] +" "+ entrada[5]
cuadro1 = c1.split()
c2 = entrada[2] +" "+ entrada[3] +" "+ entrada[6] +" "+ entrada[7]
cuadro2 = c2.split()
c3 = entrada[9] +" "+ entrada[9] +" "+ entrada[12] +" "+ entrada[13]
cuadro3 = c3.split()
c4 = entrada[10] +" "+ entrada[11] +" "+ entrada[14] +" "+ entrada[15]


print(linea1)
