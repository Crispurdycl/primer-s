print("Autor: Cristian"'\n')
"""-------------------------------------------------------------------------------------------------------------------"""

#01-DATOS DE TIPO NUMERICO
estatura = 1.65
peso = 80
complejo = 1 + 4j
print("Impresion del numero complejo: ", complejo, '\n')

"""-------------------------------------------------------------------------------------------------------------------"""

#Datos NUMERICOS ENTEROS
print(f"mi estatura es de {estatura} y mi peso es de {peso}"'\n')
#Operacion aritmetica basica
imc = peso / estatura ** 2
print("mi imc es de:",imc,'\n')
print("mi imc es de: {0:.2f}".format(imc),'\n')
print("mi imc es de: {0:.5f}".format(imc),'\n')

"""-------------------------------------------------------------------------------------------------------------------"""

#02-DATOS DE TIPO CADENA DE CARACTERES
asignatura = "Programacion"
carrera = "Ingenieria civil en informatica"
print("La asignatura de", asignatura, "es parte de la carrera de", carrera, '\n')
print(f"La asignatura de {asignatura} es parte de la carrera de {carrera} \n")
"""-------------------------------------------------------------------------------------------------------------------"""

#03-DATOS DE TIPO BOOLEANO
ampolleta = False
interruptor = True

"""-------------------------------------------------------------------------------------------------------------------"""

#con type() se puede saber el tipo de dato de una variable
print(type(ampolleta),'\n')

"""-------------------------------------------------------------------------------------------------------------------"""

#04-Datos tipo array (Objetos tipo de colección)
estudiantes =  ["Cristian", "Franco", "Matias", "Boris"]
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
deporte = ["Futbol", "Basketball", "Tenis", "Voleyball"]
ciudades = ["Santiago", "Concepcion", "Valparaiso", "Talca", "Temuco", "Puerto Montt", "Iquique", "Antofagasta", "Arica", "Copiapo", "Santiago"]
regiones = ["Los Rios", "Los Lagos", "Valparaiso", True, "str(2023)"]
lenguaje = ["Python"]
print(estudiantes, '\n')
print(num, '\n')
print(deporte, '\n')
print(ciudades, '\n')
print(regiones, '\n')
print(lenguaje, '\n')

data = ['estudiantes' , 'num', 'deporte', 'ciudades', 'regiones']
print("la cantidad de elementos de la variable data es de:", len(data))
#¿data?

#La funcion len() devuelve la cantidad de elementos de un array o de una cadena de caracteres 
print("la cantidad de letras de la palabra", estudiantes[3], "es de", len(estudiantes[3]),"caracteres"  '\n')

print("se repite una cantidad de:", ciudades.count("Santiago"), "veces" '\n')

#str para numeros
#int para cadenas de caracteres
#float para numeros decimales
#len para saber la cantidad de elementos de un array o de una cadena de caracteres
#type para saber el tipo de dato de una variable
#count para saber la cantidad de veces que se repite un elemento en un array(lista)

lenguaje = ["Javascript"]
print("nuevo valor arreglo lenguaje:", lenguaje, '\n')

print("Posicion", ciudades[2]) #no existe si se pone un numero mayor a la cantidad de elementos del array(lista) como el 11
print("Posicion", ciudades[0]) #si existe si se pone un numero menor a la cantidad de elementos del array(lista) como el 0

#reasignado el valor de la posicion 3 del array(lista) ciudades
ciudades[3] = "Rio Bueno"
print("El arreglo de ciudades es:", ciudades, '\n')

#lista de datos mixtos
datos = ["Cristian", 18, 1.65, True]

nombre, edad, estatura, estudiante = datos
print("Nombre:", nombre, '\n')
print("Edad:", edad, '\n')
print("Estatura:", estatura, "\n")
print("Estudiante:", estudiante, '\n')
print(f"el nombre es: {nombre}, la edad es: {edad}, la estatura es: {estatura}, es estudiante: {estudiante}", '\n')

print(f"Suma de listas {estudiantes + ciudades}", '\n')

print(list("Python"), '\n')
print(list(range(10)), '\n')

print(list("Cristian"), '\n')
print(list(range(12)), '\n')

print(list("Franco"), '\n')
print(list(range(6)), '\n')

####TUPLAS####
#Las tuplas son inmutables, no se pueden modificar
#Las tuplas son mas rapidas que las listas
#Las tuplas ocupan menos espacio en memoria que las listas
#Las tuplas se definen con parentesis
#las tuplas no se pueden sumar
#las tuplas no se pueden multiplicar
#las tuplas no se pueden eliminar
#las tuplas no se pueden modificar
#las tuplas no se pueden agregar elementos
#las tuplas no se pueden eliminar elementos

grupo1 = ("Cristian", 100, "Franco", 200, "Matias", 300, "Boris")
print(type(grupo1))

grupo2 = ("Franchesca", 3, "Laura", 12, "Lisa", 15, "Lorena")
print(type(grupo2))

print(grupo1[0])
print(grupo1[1])
print(grupo1[2])
print(grupo1[3])
print(grupo1[4])
print(grupo1[5])
print(grupo1[6])

#index es para saber la posicion de un elemento en una tupla o en una lista
print("El valor Franco se encuentra en la posición:", grupo1.index("Franco"))
print("El valor Matias se encuentra en la posición:", grupo1.index("Matias"))
print("El valor Boris se encuentra en la posición:", grupo1.index("Boris"))
print("El valor Cristian se encuentra en la posición:", grupo1.index("Cristian"))

grupo1 = list(grupo1)
print("La tupla es ahora de tipo:",type(grupo1), '\n')

####Set####
#Los set son colecciones de elementos desordenados
#Los set no permiten elementos duplicados
#Los set no permiten elementos mutables
#Los set no permiten elementos indexados
#Los set no permiten elementos ordenados
#los set son diccionarios sin valores
#no se puede acceder a un valor determinado porque estan desordenados, [0], [1], [30]
conjunto_vacio = set()
conjunto_vacio1 = {}
print(type(conjunto_vacio1))
print(type(conjunto_vacio))

conjunto_numeros = set({1, 2, 3, 4, 5, 6, 7, 8, 9, 10})
conjunto_marcas = {"Nike", "Adidas", "Puma", "Vans", "Converse", "Puma"}
print(conjunto_numeros)
print(conjunto_marcas)

#agregar un elemento a un set
conjunto_marcas.add("Caterpillar")
conjunto_numeros.add(190)
print(conjunto_marcas)
print(conjunto_numeros)

#eliminar un elemento de un set
conjunto_marcas.remove("Puma")
conjunto_numeros.remove(190)
print(conjunto_marcas)
print(conjunto_numeros)
