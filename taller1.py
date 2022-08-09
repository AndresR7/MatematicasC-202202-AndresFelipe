def run():
    dato1 = input("Digite varios numeros(separados por espacio): ")
    dato1 = dato1.split(',')
    dato2 = input("Digite varios numeros(separados por espacio): ")
    dato2 = dato2.split(',')
    dato1 = set(dato1)
    dato2 = set(dato2)
    operacion = input("Que operacion va a realizar(Union,interseccion,diferencia,diferencia simetrica)? ").upper()

    if operacion == "UNION":
        resultado = dato1 | dato2
        print(f'El resultado de la union es:{resultado}')
        cardinalidad = len(resultado)
        print(f'La cardinalidad es: {cardinalidad}')
    elif operacion == "INTERSECCION":
        resultado = dato1 & dato2
        print (f 'El resultado de la interseccion es: {resultado} ')
        cardinalidad = len(resultado)
        print(f'La cardinalidad es: {cardinalidad}')
    elif operacion == "DIFERENCIA":
        resultado = dato1 - dato2
        print(f'El resultado de la diferencia es:{resultado}')
        cardinalidad = len(resultado)
        print(f'La cardinalidad es: {cardinalidad}')
    elif operacion == "DIFERENCIA DECIMAL":
        resultado = dato1.symmetric_difference(dato2)
        print(f'El resultado de la diferencia decimal es:{resultado}')
        cardinalidad =len(resultado)
        print(f'la cardinalidad es: {cardinalidad}')
    else:
        print(f'Digite una opcion valida')
    if _name_ == '_main_':
        run()
