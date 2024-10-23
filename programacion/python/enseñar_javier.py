while True:
    seleccion_operacion = str(input("Escoge una operación |-Suma, |-Resta, |-Multiplicacion, |-Division, |-Resto: ")).lower()
    num1 = int(input("Dime el primer número: "))
    num2 = int(input("Dime el segundo número: "))

    if seleccion_operacion == "suma":
        suma_final = num1+num2
        print(suma_final)

    elif seleccion_operacion =="resta":
        resta_final = num1-num2
        print(resta_final)

    elif seleccion_operacion == "multiplicacion":
        multipliacion_final = num1*num2
        print(multipliacion_final)

    elif seleccion_operacion == "division":
        division_final = num1/num2
        print(division_final)
    
    elif seleccion_operacion == "fin":
        break

    elif seleccion_operacion == "resto":
        resto_final = num1%num2
        print(resto_final)
    
    else:
        print("Introduce un arugmento valido.")


