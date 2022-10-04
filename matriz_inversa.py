import copy
from itertools import count
from re import A

def matrix_format(matriz, formato):
    n_rows = len(matriz)
    n_cols = len(matriz[0])

    #Determinar el máximo ancho necesario por columna.
    col_max_width = []
    for col in range(n_cols): # Examinar la columna.
        max_width = 0 # Maximo ancho en esta columna
        for row in range(n_rows):
            # Formatear el valor en la celda para 
            # determina su ancho.
            edit_value = formato % matriz[row][col]
            max_width = max(max_width, len(edit_value))
        col_max_width.append(max_width)

    # Ahora que sabemos el ancho necesario por columna,
    # generar la matriz de salida ajustando los anchos
    # de cada valor editado.
    salida = []
    for row in range(n_rows):
        edit_row = []
        for col in range(n_cols):
            #  Primero editar el valor con su formato.
            edit_value = formato % matriz[row][col]
            #  Calcular el numero de espacios para ajustar
            #  a la derecha el valor editado
            edit_space = " "*(col_max_width[col] - len(edit_value))
            edit_row.append("%s%s" % (edit_space, edit_value))
        salida.append(edit_row)
    
    return salida

def imprimirEcuaciones(matriz_res):
    salida = matrix_format(matriz_res, " %.1f")
    for row in salida: 
        for col in row:
            print(col, end="  ")
        print("")   


def gaussJordan(a, b):
    aAux = copy.deepcopy(a)
    bAux = copy.deepcopy(b)

    n = len(bAux)

    #Se construye la matriz identidad 
    for i in range(n):
        if aAux[i][i] == 0:
            for c in range(n):
                if aAux[c][i] != 0:
                    tempA = aAux[i]
                    tempB = bAux[i]
                    aAux[i] = aAux[c]
                    aAux[c] = tempA
                    bAux[i] = bAux[c]
                    bAux[c] = tempB
                    break
        div = aAux[i][i]
        for e in range(n):
            aAux[i][e] /= div
            bAux[i][e] /= div
        for j in range(n):
            if i != j:
                fact = -aAux[j][i] / aAux[i][i]
                for k in range(n):
                    aAux[j][k] += (aAux[i][k] * fact)
                    bAux[j][k] += (bAux[i][k] * fact)
    return bAux

#Programa principal
a = []
b = []

print("| SOLUCION DE MATRICES INVERSAS POR GAUSS-JORDAN |")
dim = int(input(">>INGRESE LAS DIMENSIONES DE UNA MATRIZ CUADRADA: "))
for i in range(dim):
    newFila = []
    print("\nFILA "+str(i+1))
    for j in range(dim):
        newFila.append(int(input(">>ELEMENTO "+str(j+1)+": ")))
    a.append(newFila)
    newA = a

for j in range(dim):
    newFilaInversa = []
    for k in range(dim):
        if j == k:
            newFilaInversa.append(1)
        else:
            newFilaInversa.append(0)
    b.append(newFilaInversa)

print("\n")
x = gaussJordan(a, b)

#Se imprimen los resultados
print("MATRIZ INVERSA")
imprimirEcuaciones(x)

print()