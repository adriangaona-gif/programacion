#Ejercicio 1------------------------------------

def contar_pares(numeros):
    contador = 0
    for i in numeros: 
        if i % 2 == 0:
            contador +=1
    return contador

#Ejercicio 2-------------------------

def busqueda_max(numeros):
    max = numeros[0]
    for i in numeros: 
        if i > max:
            max = i
    return max

#Ejercicio 3--------------------------

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

#Ejercicio 4--------------------------

def suma_limit(limit):
    suma = 0
    for i in range(1, limit + 1):
        suma += i 
    return suma

#Ejercicio 5------------------

def contar_vocales(cadena):
    contador = 0
    for letter in cadena.lower():
        if letter in 'aeiou':
            contador += 1
    return contador