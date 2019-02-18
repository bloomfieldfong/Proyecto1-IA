##Unviersidad del Valle de Guatmemala
##Inteligencia Artificial
##Autor: Michelle Bloomfield Fong 16803
from conversiones import matrix, cuadros, linea
import random 
entrada = input("Ingrese los numeros del sudoku:\n")
x = matrix(entrada)


def actions(s):
    nueva = s
    cambios = []
    cuadrante = cuadros(s)
    lineas = linea(s)
    for x in range(4):
        for y in range(4):
            if s[x][y] == ".":
                pos =[x,y]

    x = 1
    while(x==1):
        random_numbers = random.sample([1,2,3,4],1)
        for z in range(4):
                ##CUADRANTE 1
            if pos[0]<2 and pos[0]<2:
                if random_numbers != lineas[pos[0]][z] and random_numbers != s[pos[0]][z] and random_numbers != cuadrante[0][z]: 
                    nueva[pos[0]][pos[1]] = random_numbers[0]
                    print(nueva)
                    x=2
                   
                ##CUADRANTE 2
            if pos[0] >2 and pos[0]<2:
                if random_numbers != lineas[pos[0]][z] and random_numbers != s[pos[0]][z] and random_numbers != cuadrante[0][z]: 
                    nueva[pos[0]][pos[1]] = random_numbers[0]
                    print(nueva)
                    x=2
                       
                ##CUADRANTE 3
            if pos[0] <2 and pos[0]>2:
                if random_numbers != lineas[pos[0]][z] and random_numbers != s[pos[0]][z] and random_numbers != cuadrante[0][z]:
                    nueva[pos[0]][pos[1]] = random_numbers[0]
                    print(nueva)
                    x=2
                        
                 ##CUADRANATE 4
            if pos[0] >2 and pos[0]>2:
                if random_numbers != lineas[pos[0]][z] and random_numbers != s[pos[0]][z] and random_numbers != cuadrante[0][z]:
                    nueva[pos[0]][pos[1]] = random_numbers[0]
                    print(nueva)
                    x=2
                
    return nueva

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