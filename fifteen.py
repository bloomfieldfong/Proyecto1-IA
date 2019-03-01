##Unviersidad del Valle de Guatmemala
##Inteligencia Artificial
##Autor: Michelle Bloomfield Fong 16803
from conversiones import matrix


def inicio():
    entrada = input("Ingrese los numeros de el juego:\n")
    problem = fifteen_puzle()
    problem.initial = matrix(entrada)
    solucion = graph_search(problem)
    ##Estado inicial

class fifteen_puzle:
    ##Defini la lista ganadora y se compara
    def goalTest(self,s):
            ganador = [['1','2','3','4'], ['5','6','7','8'], ['9','A','B','C'],['D','E','F','.']]
            if s == ganador:
                return True
            else:
                return False

    ##Acciones posibles que se puden realizar     
    def actions(self, s):
        nueva = s
        cambios = []
        
        for x in range(4):
            for y in range(4):
                if s[x][y] == ".":
                    pos = [x,y]
                    print(pos)
       
    ##Si la posicion en x no es la ultima fila el punto bajara           
        if pos[0]+1 <= 3:
            nueva[pos[0]][pos[1]] = s[pos[0]+1][pos[1]]
            nueva[pos[0]+1][pos[1]] = '.'
            cambios.append(nueva)
            return print(nueva)
        
    ##Si la posicion x no es la primera fila el punto subira
        if pos[0] - 1 >= 0:
            nueva[pos[0]][pos[1]] = s[pos[0]-1][pos[1]]
            nueva[pos[0]-1][pos[1]] = '.'
            cambios.append(nueva)
            return print(nueva)
        
    ##Si la posicion en x no es la ultima entonces se mueve hacia la derecha
        if pos[1] + 1 <=3:
            nueva[pos[0]][pos[1]] = s[pos[0]][pos[1]+1]
            nueva[pos[0]][pos[1]+1] = '.'
            cambios.append(nueva)
            return print(nueva)
        
    ##Si la posicion x no es la primera se mueve hacia la izquierda
        if pos[1]-1 <=0:
            nueva[pos[0]][pos[1]] = s[pos[0]][pos[1]-1]
            nueva[pos[0]][pos[1]-1] = '.'
            cambios.append(nueva)
            return print(nueva)
        

    def results(self,s, a):
        s_nueva = 0
        return s_nueva

    def stepCoast():
        return 
    def pathCoast():
        return
    
    ##Heuristica que nos indica cuantas filas y columnas estan bien
    def heuristica(self, matriz):
        lugar = 16
        comparacion = 1
        matriz[3][3] = '16'
        
        for i in range(4):
            for j in range(4): 
                if matriz[i][j] == str(comparacion):
                    lugar -=1
                comparacion += 1
        return lugar

inicio()