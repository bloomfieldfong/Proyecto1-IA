##Unviersidad del Valle de Guatmemala
##Inteligencia Artificial
##Autor: Michelle Bloomfield Fong 16803
from conversiones import matrix, cuadros, linea, verificarFila, verificarColumna, verificarCuadro
from search import graph_search


def inicio():
    entrada = input("Ingrese los numeros del sudoku:\n")
    problem = sudoku()
    problem.initial = matrix(entrada)
    solucion = graph_search(problem)

class sudoku:
    
    initial = "estado inicial"
    
    def actions(self,s):
        
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
                valores_posibles.append(1)
            if dos == 0:
                valores_posibles.append(2)
            if tres == 0:
                valores_posibles.append(3)
            if cuatro == 0:
                valores_posibles.append(4)
                    
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
                valores_posibles.append(1)
            if dos == 0:
                valores_posibles.append(2)
            if tres == 0:
                valores_posibles.append(3)
            if cuatro == 0:
                valores_posibles.append(4)
                
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
                valores_posibles.append(1)
            if dos == 0:
                valores_posibles.append(2)
            if tres == 0:
                valores_posibles.append(3)
            if cuatro == 0:
                valores_posibles.append(4)
                
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
                valores_posibles.append(1)
            if dos == 0:
                valores_posibles.append(2)
            if tres == 0:
                valores_posibles.append(3)
            if cuatro == 0:
                valores_posibles.append(4)
            
            return valores_posibles

    def result(self,s, a):
        
        s_nueva = 0
        for x in range(4):
            for y in range(4):
                if s[x][y] == ".":
                    pos = [x,y]
                    
        for n in range(len(a)):
            s[pos[0]][pos[1]] = str(a[n])
            s_nueva.append(s)
            
        print(s_nueva)
        return s_nueva


    ##Defini la lista ganadora y se compara
    def goalTest(self,s):
            for x in range(4):
                for y in range(4):
                    if s[x][y] == ".":
                        return False
                    else:
                        return True

    def stepCoast(self, s, a, s_nueva):
        return 1 
        
    def pathCoast(self,s_nueva):
        return len(s_nueva)

    def heuristica(self,s):
        a = 0
        for n in range(len[s]):
            new = s[n]
            for x in range(4):
                for y in range(4):
                    if new[x][y] == ".":
                        a+=1;
            return a
            
inicio()