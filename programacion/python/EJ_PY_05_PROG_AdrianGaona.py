#Ejercicio 1----------------------------

lista_num = [1,2,3,4,5]

def sumar_cinco(juegoSlitherIOenClase):
    return juegoSlitherIOenClase +5

lista_sumada = list(map(sumar_cinco,lista_num))
print(lista_sumada)


#Ejercicio 2----------------------------

list_frases = []

while True:
    frases = str(input("Introduce frases en minuscula para convertirlas en títulos: ")).lower()
    if frases == "fin":
        break
    if frases != "fin":
        list_frases.append(frases)
        
def lista_title(frases):
    return frases.title()

lista_final = list(map(lista_title,list_frases))
print(lista_final)

#Ejercicio 3----------------------------

lista_num = []

while True:
    numeros = int(input("Introduce los números que quieres doblar, introduce 0 para terminar: "))
    if numeros > 0:
        lista_num.append(numeros)
    elif numeros <0: 
        lista_num.append(numeros)
    elif numeros == 0:
        break

def lista_num2(listanum):
    return listanum * 2

lista_final = list(map(lista_num2, lista_num))
print(lista_final)

#Ejercicio 4----------------------------

lista_decimales = []

while True:
    numeros = float(input("Introduce numeros decimales, siendo 0 el número utilizado para finalizar: "))
    if numeros > 0:
        lista_decimales.append(numeros)
    elif numeros < 0: 
        lista_decimales.append(numeros)
    elif numeros == 0:
        break

def lista_decimales2(numeros):
    return round(numeros)

lista_decimales_final = list(map(lista_decimales2, lista_decimales))
print (lista_decimales_final)

#Ejercicio 5----------------------------
lista = []

while True:
    palabras = str(input("Introduce palabras siendo fin la palabra para finalizar la cuenta: ")).lower()
    if palabras == "fin":
        break
    if palabras != "fin":
        lista.append(palabras)
    
def lista_longitud(palabras):
    return len(palabras)

lista_final_len = list(map(lista_longitud, lista))
print(lista_final_len)