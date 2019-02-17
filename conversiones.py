        
def conversion(x):
    for i in range(4):
        for j in range(0,4):
            if x[i][j] == 'A':
                x[i][j] = '10'        
            if x[i][j] == 'B':
                x[i][j] = '11'
            if x[i][j] == 'C':
                x[i][j] = '12'
            if x[i][j] == 'D':
                x[i][j] = '13'
            if x[i][j] == 'E':
                x[i][j] = '14'
            if x[i][j] == 'F':
                x[i][j] = '15'
    return x

def matrix(entrada):
    if len(entrada) == 16:
        l1 = entrada[0] +" "+ entrada[1] +" "+ entrada[2] +" "+ entrada[3]
        linea1 = l1.split()
        l2 = entrada[4] +" "+ entrada[5] +" "+ entrada[6] +" "+ entrada[7]
        linea2 = l2.split()
        l3 = entrada[8] +" "+ entrada[9] +" "+ entrada[10] +" "+ entrada[11]
        linea3 = l3.split()
        l4 = entrada[12] +" "+ entrada[13] +" "+ entrada[14] +" "+ entrada[15]
        linea4= l4.split()
        return conversion([linea1,linea2,linea3,linea4])
    else:
        print("INVALIDO")


def cuadrantes(entrada):
    if len(entrada) == 16:
        c1 = entrada[0] +" "+ entrada[1] +" "+ entrada[4] +" "+ entrada[5]
        cuadro1 = c1.split()
        c2 = entrada[2] +" "+ entrada[3] +" "+ entrada[6] +" "+ entrada[7]
        cuadro2 = c2.split()
        c3 = entrada[9] +" "+ entrada[9] +" "+ entrada[12] +" "+ entrada[13]
        cuadro3 = c3.split()
        c4 = entrada[10] +" "+ entrada[11] +" "+ entrada[14] +" "+ entrada[15]
    else: 
        print("INVALIDO")
        

                
                
            
                