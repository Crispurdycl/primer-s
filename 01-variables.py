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
#Se imprime variables con comas (,) y con signo de suma (+) y con la funcion str() para convertir un numero a cadena de caracteres
#Se imprime variables con la funcion format() y con la funcion f"" para imprimir variables dentro de un string 
print("Hola, soy", nombre, nombre2, apellido, apellido2, "y tengo", edad, "años")
print("Hola, soy" + " " + nombre + " " + nombre2 + " " + apellido + " " + apellido2 + " " + "y tengo" + " " + str(edad) + " " + "años")
print(f"Hola, soy {nombre} {nombre2} {apellido} {apellido2} y tengo {edad} años")

#Actualizacion de variables
nombre = "Matias"

apellido = "Guzman"
print("Hola mi nuevo nombre es", nombre, apellido)

nombre = input("¿Cual es tu nombre?:\n ")
print("tu nombre es:", nombre, "y tiene", len(nombre), "caracteres")

#Variables en una sola linea (separadas por coma)
Ciudad, region, pais, año = "Santiago", "Metropolitana", "Chile", 2023
print("yo naci en", Ciudad, "de la region", region, "del pais", pais, "el año", str(2023))