# ------------------------------------------------------------Ejercicio 1:----------------------------------------------------

# Creamos un bucle para que repita todo el rato la "opcion" hasta que pulsemos 3 (salir).
while True:
    opcion = int(input("Elige un tipo de figura (1 - Cuadrado 2- Rectángulo 3- Salir): "))

#Creamos un if que diga que si la opción es 1, el usuario ingrese los lados del cuadrado.
    if opcion == 1:
        lado_cuadrado1 = int(input("\nDame el lado del cuadrado: "))
        lado_cuadrado2 = int(input("\nDame el segundo lado del cuadrado: "))

#Como un cuadrado tiene los 2 lados iguales, si el usuario ingresa diferentes lados, el programa dara error.
        if lado_cuadrado1 != lado_cuadrado2:
            print("\nNo pueden tener lados diferentes, eso es un rectángulo.")
        
#Si los lados son iguales, el programa procede.       
        if lado_cuadrado1 == lado_cuadrado2:
            area_cuadradofinal = lado_cuadrado1 * lado_cuadrado2
            print(f"\nEl área del cuadrado es {area_cuadradofinal}")
            perimetro_cuadradofinal = (lado_cuadrado1*2) + (lado_cuadrado2*2)
            print(f"\nEl perímetro del cuadrado es {perimetro_cuadradofinal}")

#Creamos un for para que segun el numero que pongamos en "lado_cuadrado1", nos haga las filas para la figura.
            for i in range(0,lado_cuadrado1):
                i = lado_cuadrado1 * "*"
                i = lado_cuadrado2 * "*"
                print(i)


#Lo mismo con el rectángulo.
    elif opcion == 2:
        altura_rectángulo = int(input("\nDame la altura del rectángulo: "))
        base_rectángulo = int(input("\nDame la base del rectángulo: "))

#Un rectángulo no tiene que tener la misma base que altura, si no, sería un cuadrado.
        if altura_rectángulo == base_rectángulo:
            print("\nNo pueden tener los mismos lados, eso es un cuadrado.")

#Si la base != a la altura, podemos proceder.
        if altura_rectángulo != base_rectángulo:
            area_rectangulofinal = altura_rectángulo * base_rectángulo
            perimetro_rectangulofinal = (altura_rectángulo*2) + (base_rectángulo*2)
            print(f"\nEl área del rectángulo es {area_rectangulofinal}")
            print(f"\nEl perímetro del rectángulo es {perimetro_rectangulofinal}")

#Creamos un for para que nos haga un print de "*" dependiendo de la base y la altura que especifiquemos.
            for i in range(0,altura_rectángulo):
                i = altura_rectángulo * "*"
                i = base_rectángulo * "*"
                print(i)

#Creamos una tercera opción para subir nota, en la que podremos salir del bucle while y "salir del sistema".
    elif opcion == 3:
        print("\nSaliendo del sistema...")
        break        
#Por último hacemos un else para en caso de que el usuario escoja "4", que le diga que escoja una opción válida.
    else:
        print("\nElige una opción correcta.")

# ------------------------------------------------------------Ejercicio 2:------------------------------------------------------

# Para empezar ponemos "import random" para el correcto funcionamiento de "random.randit"
import random

# Después de poner input para guardar la elección dentro de "valor", vamos a decir que en eleccion_random se guarde un
# numero aleatorio del 1 al 3.

eleccion_random = random.randint(1,3)

# Clasificamos cada opción en cada numero correspondiente.
piedra = 1
papel = 2
tijera = 3

#Añadimos contadores para mas nota jeje
contador_humano = 0
contador_npc = 0

# Y creamos el bucle.
while contador_humano != 3 and contador_npc != 3:
    valor = int(input("\nElige (1-Piedra|2-Papel|3-Tijera): "))
    
# En caso de que las elecciones sean iguales.------------------
    if eleccion_random == 1 and valor == 1:
        eleccion_random = random.randint(1,3)
        print("El npc ha elegido piedra")
        print("Has elegido piedra, empate.")
        
    elif eleccion_random == 2 and valor == 2:
        eleccion_random = random.randint(1,3)
        print("El npc ha elegido papel")
        print("Has elegido papel, empate.")
    
    elif eleccion_random == 3 and valor == 3:
        eleccion_random = random.randint(1,3)
        print("El npc ha elegido tijera")
        print("Has elegido tijera, empate.")

#Esta parte es para cuando las elecciones son diferentes.------
    elif eleccion_random == 1 and valor == 2:
        eleccion_random = random.randint(1,3)
        print("El npc ha elegido piedra")
        print("Has elegido papel, has ganado!")
        contador_humano = contador_humano + 1
        print(f"llevas {contador_humano} partidas ganadas.")
    
    elif eleccion_random == 2 and valor == 1:
        eleccion_random = random.randint(1,3)
        print("El npc ha elegido papel")
        print("Has elegido piedra, has perdido.")
        contador_npc = contador_npc + 1
        print(f"El npc lleva {contador_npc} partidas ganadas.")
    
    elif eleccion_random == 1 and valor == 3:
        eleccion_random = random.randint(1,3)
        print("El npc ha elegido piedra")
        print("Has elegido tijera, has perdido.")
        contador_npc = contador_npc + 1
        print(f"El npc lleva {contador_npc} partidas ganadas.")

    elif eleccion_random == 3 and valor == 1:
        eleccion_random = random.randint(1,3)
        print("El npc ha elegido tijera")
        print("Has elegido piedra, has ganado!")
        contador_humano = contador_humano + 1
        print(f"llevas {contador_humano} partidas ganadas.")

    elif eleccion_random == 2 and valor == 3:
        eleccion_random = random.randint(1,3)
        print("El npc ha elegido papel")
        print("Has elegido tijera, has ganado!")
        contador_humano = contador_humano + 1
        print(f"llevas {contador_humano} partidas ganadas.")

    elif eleccion_random == 3 and valor == 2:
        eleccion_random = random.randint(1,3)
        print("El npc ha elegido tijera")
        print("Has elegido papel, has perdido.")
        contador_npc = contador_npc + 1
        print(f"El npc lleva {contador_npc} partidas ganadas.")

    else:
        print("\nIntroduce un argumento válido.")
        break

#Salimos del bucle, y para finalizar le decimos al programa que si cualquiera de los dos ha llegado a 3 partidas ganadas,
#lo muestre y finalice la partida.
if contador_humano == 3:
        print("\nHas llegado a 3 partidas ganadas, has ganado!")
    
elif contador_npc == 3:
        print("\nEl npc ha llegado a 3 partidas ganadas, has perdido.")





# ------------------------------------------------------------Ejercicio 3:-------------------------------------------------------

# Empezamos con un while true para crear un bucle que haga que si tu saldo inicial es menor que 0, 
# te pida que ingreses el saldo correcto.
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
    

