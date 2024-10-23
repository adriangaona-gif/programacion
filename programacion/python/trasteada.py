# frase= "Me loopeo al killer y se marea"
# longitud= len(frase)
# print(longitud)




# frase= "Uno"
# longitud= len(frase)
# print(longitud)



while True:
    
    saldo_inicial = float(input("\nDime el saldo inicial de tu cuenta: "))

    if saldo_inicial < 0:
        print("Ingresa un saldo correcto.")

    elif saldo_inicial > 0:
        break

#Una vez el saldo sea correcto, creamos los contadores para subir nota y después el bucle while.
contador_ingresos = 0
contador_retiradas = 0
while True:

#Decimos al usuario con un input que elija el movimiento que quiere realizar en su cuenta y creamos las opciones.
    opciones = int(input("\nElige un movimiento |1-Ingresar dinero, |2-Retirar dinero, |3-Mostrar saldo, |4-Salir, |5-Estadísticas: "))

    if opciones == 1:
        ingresar_dinero = float(input("\nIngresa la cantidad de dinero a ingresar: "))
        saldo_inicial = saldo_inicial + ingresar_dinero
        contador_ingresos = contador_ingresos + 1

    elif opciones == 2:
        retirar_dinero = float(input("\nIngresa la cantidad de dinero a retirar: "))
        saldo_inicial = saldo_inicial - retirar_dinero
        contador_retiradas = contador_retiradas + 1   
        
    elif opciones == 3: 
        print(f"\nEste es tu saldo: {saldo_inicial}")
        
    elif opciones == 4:
        print("\nSaliendo del sistema...")
        break

#Por útlimo, añadimos el último elif para mostrar en pantalla el contador de ingresos y retiradas totales.
    elif opciones == 5:
        print(f"\nTus ingresos totales han sido: {contador_ingresos}")
        print(f"Tus retiradas totales han sido: {contador_retiradas}")