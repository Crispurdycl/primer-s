# Crear un algoritmo que solicite por consola las 3 notas de los laboratorios realizados en el ramo de Programación. Luego obtener el promedio ponderado de la
# siguiente manera:
# Promedio Ponderado = Lab1 * 0,3 + Lab2 * 0,4 + Lab3 * 0,3
# Si el promedio es menor a 4,0 debe imprimir el mensaje que el estudiante reprobó
# la asignatura. Si el promedio es superior a 4,0, indicar que el estudiante aprobo
# la asignatura. Si la nota es superior 6,0, debe mostrar el mensaje: el estudiante
# aprobo con distinción.

lab1 = float(input("Ingrese la nota del primer laboratorio: "))
lab2 = float(input("Ingrese la nota del segundo laboratorio: "))
lab3 = float(input("Ingrese la nota del tercer laboratorio: "))

promedio = lab1*0.3 + lab2*0.4 + lab3*0.3

if promedio < 4:
    print("El estudiante reprobo la asignatura con: ", promedio)
elif promedio > 4 and promedio < 6:
    print("El estudiante aprobo la asignatura")
else:
    print("El estudiante aprobo con distincion")