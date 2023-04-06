"""Este es un ejemplo"""

#Esta es una impresion en pantalla
print("Hola, soy Cristian!")

#Se crean varias variables
nombre = "Cristian"

nombre2 = "Andres"

apellido = "Cárdenas"

apellido2 = "Lagos"

edad = 18

#Se imprime el valor de la variable con un mensaje
print("Hola, soy", nombre, nombre2, apellido, apellido2, "y tengo", edad, "años")
print("Hola, soy" + " " + nombre + " " + nombre2 + " " + apellido + " " + apellido2 + " " + "y tengo" + " " + str(edad) + " " + "años")

#Actualizacion de variables
nombre = "Matias"

apellido = "Guzman"
print("Hola mi nuevo nombre es", nombre, apellido)

nombre = input("¿Cual es tu nombre?:\n ")
print("tu nombre es:", nombre, "y tiene", len(nombre), "caracteres")