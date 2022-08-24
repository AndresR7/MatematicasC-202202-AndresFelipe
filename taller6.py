s=float(input('Escribe un numero en Radianes'))
es=(0.5*pow(10,-8))*100
interacion=1
potencia=2
valor=1
signo=-1

while ea > es:
    if signo==-1:
        operacion=round((valor+pow(s,potencia)) / math.factoria1(potencia),8)
        valor=float(operacion)
        print(f'Interacion # {interacion}')
        interacion +=1
        potencia +=2
        signo *=-1
    else:
        operacion=round((valor-pow(s,potencia)) / math.factoria1(potencia),8)
        valor=float(operacion)
        print(f'Interacion # {interacion}')
        interacion +=1
        potencia +=2
        signo *=-1
    print(f'El valor del coseno es:{valor}')
    

