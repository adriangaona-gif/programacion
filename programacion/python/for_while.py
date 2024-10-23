

# contador = 0

# while contador < 5:
#     print(contador)
#     contador += 1

#------------------------------------------------------------------
                            #EJERCICIO 1
#------------------------------------------------------------------

# numero = int(input("Dame un numero entero: "))

# if numero < 0:
#     print("Elige un numero entero valido")

# else:
#     contador = 0
#     for numero in range(1,numero+1):
#         if numero %2 == 0:
#             contador += 1
#     print("Hay", contador, "numeros pares entre 1 y", numero)
         


#------------------------------------------------------------------
                            #EJERCICIO 2
#------------------------------------------------------------------

# num = int(input("Dame un numero entero postiivo: "))
# suma = num
# while num > 0:
#     num = int(input("Dame otro numero entero positivo: "))
#     if num < 0:
#         break
#     suma += num
# # if num < 0:
# print("La suma total es: ",suma)

#------------------------------------------------------------------
                            #EJERCICIO 3
#------------------------------------------------------------------

# num = int(input("Dame un numero entero positivo: "))
# contador = 0
# if num > 0: 
#     for numero in range(1,11):
#         numero = num * numero
#         contador += 1
#         print(num, "X", contador, "=", numero)
# else:
#     print("Dame un numero positivo, ese es negativo payaso")

#------------------------------------------------------------------
                            #EJERCICIO 4
#------------------------------------------------------------------
import random
num = random.randint(1,10)

ingresa = int(input("Ingresa un numero, a ver si adivinas... : "))
while ingresa != num:
    if ingresa < num :
        print("Mas alto...")
    elif ingresa > num:
        print("Mas bajo...")
           
    ingresa = int(input("Ingresa un numero, a ver si adivinas... : "))

print(f"Felicidades, lo has adivinado,el numero secreto era {num}!")