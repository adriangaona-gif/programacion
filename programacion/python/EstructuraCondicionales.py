# edad = 15
# es_estudiante = True

# if edad < 18 and es_estudiante:
#         print("Es un estudiante menor de edad")
# elif edad < 18 and not es_estudiante:
#         print("Es menor de edad pero no es estudiante")
# else:
#         print("Es mayor de edad")

#--------------------------------------------------------
#--------------------------------------------------------

# edad = int(input("Cuantos años tienes?: "))

# if edad >=0 and edad < 5:
#     print("La entrada es gratuita")
# elif edad >=5 and edad <= 12:
#     print("La entrada cuesta 5€")
# elif edad >=13 and edad <= 17:
#     print("La entrada cuesta 7€")
# elif edad >=18:
#     print("La entrada cuesta 10€")
# else:
#     print("Ingresa un numero valido")

#--------------------------------------------------------
#--------------------------------------------------------

# nota = int(input("Que nota ha sacado?: "))
# if nota >= 90 and nota <=100:
#         print("La calificacion es A")
# elif nota >=80 and nota <90:
#         print("La calificacion es B")
# elif nota >=70 and nota<80: 
#         print("La calificacion es C")
# elif nota >=60 and nota<70: 
#         print("La calificacion es D")
# elif nota <60:
#         print("La calificacion es F")

# else:
#         print("Ingresa una calificacion valida")

#--------------------------------------------------------
#--------------------------------------------------------

# dia =  int(input("Ingresa un número del 1-7 para mostrar el dia de la semana: "))

# match dia:
#         case 1:
#                 print("Lunes")
#         case 2:
#                 print("Martes")
#         case 3: 
#                 print("Miércoles")
#         case 4 :
#                 print("Jueves")
#         case 5: 
#                 print("Viernes")
#         case 6: 
#                 print("Sábado")
#         case 7: 
#                 print("Domingo")


#--------------------------------------------------------
#--------------------------------------------------------

# edad = int(input("Dime cual es tu edad: "))

# if edad >=0 and edad <12: 
#     print("Niño")
# elif edad >=12 and edad <=17:
#     print("Adolescente")
# elif edad >=18 and edad <=59:
#     print("Adulto")
# elif edad >= 60:
#     print("Adulto mayor")
# else:
#     print("Ingresa un número valido.")


# idioma = str(input("Dime cual es tu preferencia de idioma: "))

# match idioma:
#         case "es":
#                 print("Hola, este es un texto en español.")
#         case "en":
#                 print("Hello, this is a text in english")
#         case "fr":
#                 print("Bonjour, ceci est un texte en français")
#         case _:
#                 print("Idioma no soportado")
        
      
#--------------------------------------------------------
#--------------------------------------------------------

# vehiculo = str(input("Selecciona un tipo de vehículo (- coche - moto - bicicleta): "))
# vehiculo_pepe = vehiculo.lower()

# color = str(input("Elige el tipo de color (-rojo -azul -verde): "))
# color_pepe = color.lower()


# if vehiculo_pepe == "coche":
#         print("Vehíchulo de cuatro ruedas")
# elif vehiculo_pepe == "moto":
#         print("Vehículo de dos ruedas")
# elif vehiculo_pepe == "bicicleta":
#         print("Vehículo no motorizado")
# else:
#         print("Tipo de vehículo no reconocido.")


# match color_pepe:
#         case "rojo": 
#                 print("Has elegido el color rojo")
#         case "azul":
#                 print("Has elegido el color azul")
#         case "verde":
#                 print("Has elegido el color verde")
#         case _:
#                 print("Elige un color válido.")


