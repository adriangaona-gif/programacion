#EJERCICIO 1-------------------------------------
# def calcular_area_circulo(area):
#     area = 3.14 * radio*radio
#     print("El área del circulo es: ", area )

# radio = float(input("Ingresa el radio del círculo: "))
# calcular_area_circulo(radio)

#EJERCICIO 2-------------------------------------
def contar_vocales(cadena):
    vocales = ["a","e","i","o","u", "A", "E", "I", "O", "U"]
    contador_vocales = 0
    for vocales2 in cadena:
        if vocales2 in vocales:
            contador_vocales = contador_vocales+1
        print("La cadena tiene un total de: ", contador_vocales, "vocales.")
