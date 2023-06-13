#Definimos variables

estudiante = input("Ingrese nombre del estudiante: ")
carrera = input("Ingrese carrera del estudiante: ")
NotaLab1 = float(input("Ingrese nota del laboratorio 1: "))
NotaLab2 = float(input("Ingrese nota del laboratorio 2: "))

#asignamos nuestro diccionario

ICINF = [ estudiante, carrera, NotaLab1, NotaLab2 ]

#calculamos el promedio de notas

NotasLabs = NotaLab1*0.3 + NotaLab2*0.7

#imprimimos el diccionario y el promedio de notas

print(ICINF, "\n")
print(f"su promedio de notas es {NotasLabs:.1f}".format(NotasLabs))
input(print("Presione cualquier tecla para salir"))
#fin del programa