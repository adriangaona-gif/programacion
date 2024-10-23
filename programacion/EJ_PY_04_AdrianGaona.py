#EJERCICIO 1----------------------------------------





#EJERCICIO 2--------------------------------------------------






#EJERCICIO 3--------------------
def es_primo(numero):
    if numero > 1:
        if numero % numero+1 == 0:
            print("No es primo")
        elif (numero % 1 == 0) and (numero % numero == 0):
            print("Es primo")
        else:
            print("Menor que 1, el número no puede ser primo")

#(PROGRAMA PRINCIPAL)
numero = int(input("Intorduce un número entero para averiguar si el número es primo o no, (utilizando '0' como el número final): "))

es_primo(numero)

#SOLUCIÓN DEL EJERCICIO 3 CON "RETURN"--------------------------------------
def es_primo(numero):
    valor_devuelto = False
    if numero > 1:
        if numero % numero+1 == 0:
            valor_devuelto = False
        elif (numero % 1 == 0) and (numero % numero == 0):
            valor_devuelto = True
    else:
        valor_devuelto = False
    return valor_devuelto

##Programa principal empieza aqui
numero = int(input("Introduce un número entero para averiguar si el número es primo o no, (utilizando '0' como el número final): "))

valor_funcion = es_primo(numero)

if valor_funcion == True:
    print('Es primo')
else:
    print('No es primo')