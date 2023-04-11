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
print("la cantidad de letras de la palabra", estudiantes[0], "es de", len(estudiantes[0]),"caracteres"  '\n')

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
ciudades[3] = "Talcahuano"
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