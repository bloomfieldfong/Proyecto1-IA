##Unviersidad del Valle de Guatmemala
##Inteligencia Artificial
##Autor: Michelle Bloomfield Fong 16803
from conversiones import matrix, cuadros, linea, verificarFila, verificarColumna, verificarCuadro

entrada = input("Ingrese los numeros del sudoku:\n")
x = matrix(entrada)

def actions(s):
    
    valores_posibles= []
    valores_presentes =[]
    pos = []
    
    cuadrante = cuadros(s)
    lineas = linea(s)
    
    uno = 0
    dos = 0
    tres = 0
    cuatro = 0
    for x in range(4):
        for y in range(4):
            if s[x][y] == ".":
                pos = [x,y]
           
           ##CUADRANTE 1 
    if pos[0]<=2 and pos[1]<=2:
        nodo = lineas[y] + s[x] + cuadrante[0]

        ##calcula los valores existentes que estan en los cuadrantes, lineas y columnas
        for n in nodo:
            if n not in valores_presentes:
                valores_presentes.append(n)
        
        ##Verifica el numero que no existe      
        for a in range(len(valores_presentes)):
            if valores_presentes[a] == '1':
                uno+=1
            if valores_presentes[a] == '2':
                dos+=1
            if valores_presentes[a] == '3':
                tres+=1
            if valores_presentes[a] == '4':
                cuatro+=1
               
        if uno == 0:
            valores_posibles.append('1')
        if dos == 0:
            valores_posibles.append('2')
        if tres == 0:
            valores_posibles.append('3')
        if cuatro == 0:
            valores_posibles.append('4')
                
            ##CUADRANTE 2
    if pos[0] >=2 and pos[1]<=2:
        nodo = lineas[y] + s[x] + cuadrante[3]
        
        ##calcula los valores existentes que estan en los cuadrantes, lineas y columnas
        for n in nodo:
            if n not in valores_presentes:
                valores_presentes.append(n)
        
        ##Verifica el numero que no existe 
        for a in range(len(valores_presentes)):
            if valores_presentes[a] == '1':
                uno+=1
            if valores_presentes[a] == '2':
                dos+=1
            if valores_presentes[a] == '3':
                tres+=1
            if valores_presentes[a] == '4':
                cuatro+=1
               
        if uno == 0:
            valores_posibles.append('1')
        if dos == 0:
            valores_posibles.append('2')
        if tres == 0:
            valores_posibles.append('3')
        if cuatro == 0:
            valores_posibles.append('4')
            
            ##CUADRANTE 3
    if pos[0] <=2 and pos[1]>=2:
        nodo = lineas[y] + s[x] + cuadrante[2]
        
        ##calcula los valores existentes que estan en los cuadrantes, lineas y columnas
        for n in nodo:
            if n not in valores_presentes:
                valores_presentes.append(n)
                
        ##Verifica el numero que no existe 
        for a in range(len(valores_presentes)):
            if valores_presentes[a] == '1':
                uno+=1
            if valores_presentes[a] == '2':
                dos+=1
            if valores_presentes[a] == '3':
                tres+=1
            if valores_presentes[a] == '4':
                cuatro+=1
               
        if uno == 0:
            valores_posibles.append('1')
        if dos == 0:
            valores_posibles.append('2')
        if tres == 0:
            valores_posibles.append('3')
        if cuatro == 0:
            valores_posibles.append('4')
            
            ##CUADRANATE 4
    if pos[0] >=2 and pos[1]>=2:
        nodo = lineas[y] + s[x] + cuadrante[3]
        
        ##calcula los valores existentes que estan en los cuadrantes, lineas y columnas
        for n in nodo:
            if n not in valores_presentes:
                valores_presentes.append(n)
           
        ##Verifica el numero que no existe 
        for a in range(len(valores_presentes)):
            if valores_presentes[a] == '1':
                uno+=1
            if valores_presentes[a] == '2':
                dos+=1
            if valores_presentes[a] == '3':
                tres+=1
            if valores_presentes[a] == '4':
                cuatro+=1
               
        if uno == 0:
            valores_posibles.append('1')
        if dos == 0:
            valores_posibles.append('2')
        if tres == 0:
            valores_posibles.append('3')
        if cuatro == 0:
            valores_posibles.append('4')
  

def results(a, s):
    return


##Defini la lista ganadora y se compara
def goalTest(s):
        ganador = [['1','2','3','4'], ['5','6','7','8'], ['9','A','B','C'],['D','E','F','.']]
        if s == ganador:
            return True
        else:
            return False

def stepCoast(s, a, i):
    return

def pathCoast():
    return
        
actions(x)