print("Autor: Cristian")
"""-------------------------------------------------------------------------------------------------------------------"""
#01-DATOS DE TIPO NUMERICO
estatura = 1.65
peso = 80
complejo = 1 + 4j
print("Impresion del numero complejo: ", complejo)
"""-------------------------------------------------------------------------------------------------------------------"""
#Operacion aritmetica basica
imc = peso / estatura ** 2
print("mi imc es de:", imc )
"""-------------------------------------------------------------------------------------------------------------------"""
#02-DATOS DE TIPO CADENA DE CARACTERES
asignatura = "Programacion"
carrera = "Ingenieria civil en informatica"
print("La asignatura de", asignatura, "es parte de la carrera de", carrera)
"""-------------------------------------------------------------------------------------------------------------------"""
#03-DATOS DE TIPO BOOLEANO
ampolleta = False
interruptor = True
"""-------------------------------------------------------------------------------------------------------------------"""
#con type() se puede saber el tipo de dato de una variable
print(type(ampolleta))
"""-------------------------------------------------------------------------------------------------------------------"""
#04-Datos tipo array (Objetos tipo de colección)
estudiantes =  ["Cristian", "Franco", "Matias", "Boris"]
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(estudiantes)
print(num)