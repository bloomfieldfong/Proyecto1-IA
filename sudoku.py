##Unviersidad del Valle de Guatmemala
##Inteligencia Artificial
##Autor: Michelle Bloomfield Fong 16803
from conversiones import matrix, cuadros, linea, verificarFila, verificarColumna, verificarCuadro
from search import graph_search

##Entrada inicial de nuestros datos
def inicio():
    entrada = input("Ingrese los numeros del sudoku:\n")
    problem = sudoku()
    problem.initial = matrix(entrada)
    solucion = graph_search(problem)
    print(actions(problem.initial))

class sudoku:
    
    ##Definicion de nuestro estado inicial
    initial = "estado inicial"
    
    ##Definicion de nuestras acciones
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
        
        ##Nos indica en que posicion esta el ultimo punto
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
            
            ##Si no existe uno de los numeros agrega a valores_posibles el numero       
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
            ##Si no existe uno de los numeros agrega a valores_posibles el numero          
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
            ##Si no existe uno de los numeros agrega a valores_posibles el numero         
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
            
            ##Si no existe uno de los numeros agrega a valores_posibles el numero         
            if uno == 0:
                valores_posibles.append(1)
            if dos == 0:
                valores_posibles.append(2)
            if tres == 0:
                valores_posibles.append(3)
            if cuatro == 0:
                valores_posibles.append(4)
            
            print(valores_posibles)
            return valores_posibles

    
        
    ##Result recibe una matriz y la accion que se puede hacer con la matriz
    def result(self,s, a):    
        s_nueva = 0
        
        ##ultima posicion del punto 
        for x in range(4):
            for y in range(4):
                if s[x][y] == ".":
                    pos = [x,y]
        
        ##cambia los puntos por los posibles valores            
        
        s[pos[0]][pos[1]] = str(a)
        s_nueva.append(s)     
        print(s_nueva)
        return s_nueva


    ##Defini que el goalTest es cuando ya no hay un punto en la matriz
    def goalTest(self,s):
            for x in range(4):
                for y in range(4):
                    if s[x][y] == ".":
                        return False
                    else:
                        return True
    
    ##por cada cambio que se haga se le asgina de costo 1 
    def stepCoast(self, s, a, s_nueva):
        return 1 
    
    ##
    def pathCoast(self,s_nueva):
        return len(s_nueva)

    def heuristica(self,p):
        a = 0
        s = p[len(p)-1]
        for n in range(len[s]):
            new = s[n]
            for x in range(4):
                for y in range(4):
                    if new[x][y] == ".":
                        a+=1;
            return a
    
    def criteria(self, frontera):
        for path in frontera:
            z = heuristica(path) + pathCoast(path)
        return z
      

        
inicio()