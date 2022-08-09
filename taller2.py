
from multiprocessing.managers import _Namespace

def union(A, B):
    C = A | B
    return C

def interseccion(A, B):
    C = A & B
    return C

def diferencia(A, B):
    C = A - B
    return C

def dif_simetrica(A, B):
    C = (A | B) - (A & B)
    return C

def run()
conjuntoA = set({6,7,8,9,10,11,12,13,14,15,16,17,18,19,20})
conjuntoB = set({2,4,6,8,10,12,14,16,18,20,22,24})
conjuntoC = set({1,4,8,10,12,15,18,20})
conjuntoD = set({2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41})

rta1 = interseccion(conjuntoB, dif_simetrica(conjuntoC, conjuntoD))
    print(f
' La interseccion del conjuntoB y la diferencia simetrica entre el conjuntoC y el conjuntoD  es: {rta1}')
    elif pregunta = 2:
rta2 = interseccion(conjuntoA,conjuntoC,union(conjuntoB))
     print(f
'La interseccion de la union entre el conjuntoA y el conjuntoC con el conjuntoB  es: {rta2}')
    elif pregunta = 3:
rta3= union(conjuntoB,conjuntoD,diferencia(conjuntoC))
    print(f
'La union del conjuntoB y el conjuntoD con la diferencia del conjuntoC es: {rta3}')
    elif pregunta = 4:
rta4 = dif_simetrica ( diferencia(conjuntoA,conjuntoB),interseccion(conjuntoA,conjuntoD))
    print(f 
'La diferencia simetrica de la union  entre el conjuntoA y el conjuntoD con la diferencia del conjuntoA y el conjuntoB es:{rta4}')
    else:
        print(f 'Digite una opcion que sea valida')
if __name__ ='_main_':
run()






