# A) Concatenar todas las listas e imprimir la lista obtenida.
# B) Agregar el número 20 en la penúltima posición de la lista.
# C) Ordenar la lista de forma descendente.
# D) Insertar la lista [4,5,6] en la última posición de la lista ordenada
# E) Sumar todos los números dentro de la lista.
# F) Obtener el promedio simple de la lista.

a = [21,8,15,3,12]
b = [10,9,12,15,18]
c = [2,3,8,9,12]
d2s = a + b + c

#imprimimos y agregamos a otra lista
print(f"La suma de las listas seria: \n {d2s}")

#agregamos el numero a la lista vacia

d2s.insert(14, 20)
print(f"Agregamos el numero 20 a la penultima posicion de la lista \n {d2s}")

#ordenamos la lista de forma descendente

d2s.sort(reverse=True)
print(d2s)

#insertamos la lista [4,5,6] en la ultima posicion de la lista ordenada

ef = [4, 5, 6]
d3s = d2s + ef

print(d3s)

#sumamos todos los numeros dentro de la lista

suma = sum(d3s)
print(suma)

#obtenemos el promedio simple de la lista

promedio = suma / len(d3s)
print(promedio)
print("fin")