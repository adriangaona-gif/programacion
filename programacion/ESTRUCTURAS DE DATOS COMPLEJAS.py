# lista1=[1,2,3,4]

# tupla1=(1,2,3,4)


# # print("Valor de la lista")
# # print(lista1)

# # print("Valor de la tupla")
# # print(tupla1)

# lista1[0] = 10
# print("Valor de la lista")
# print(lista1)

#Las tuplas no se pueden editar porque son inmutables

# dic1 = {}

# nombre = input("Introduce el nombre del nuevo contacto: ")
# telefono = input(f"Introduce el teléfono de {nombre}: ")

# dic1 [nombre] = telefono #Insertamos un nuevo par clave/valor en el diccionario

# print("Esta es tu agenda")
# print(dic1)

# print("Vamos a modificar el teléfono de un contacto. ")
# nombre_busqueda = input("Dame el nombre del contacto que quieres cambiar: ").lower()
# telefono_nuevo = input("Dame el nuevo número de teléfono: ")

# dic1[nombre_busqueda] = telefono_nuevo
# print(dic1)






# EJERCICIOS---------------------------------------------------------------------------------


lista_reproduccion = []

#permitir al usuario introducir nombres de canciones hasta que el nombre sea fin
#el objetivo es tener una lista de reproducción similar a esta:
#lista_reproduccion['Paquito chocolatero', 'Tengo un tractor amarillo']

cancion = input('Dame el nombre de una canción: ')

while cancion != 'fin':
    lista_reproduccion.append(cancion)
    cancion = input('Dame el nombre de una canción: ').lower()


print (lista_reproduccion)

#mostrar mi lista de reproducción y permitir al usuario introducir el número de la canción que quiere escuchar

for i in range(len(lista_reproduccion)):
    print(f"{i}.- {lista_reproduccion[i]}")
    #print(lista_reproduccion[i])

cancion_a_reproducir = int(input("Dime el número de canción que deseas escuchar: "))

print(f"Estas escuchando la canción: {lista_reproduccion[cancion_a_reproducir]}")


#----------------------------------------------------------------
