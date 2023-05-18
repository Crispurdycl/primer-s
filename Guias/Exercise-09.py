# . Se tiene la siguiente lista de enteros:
# numeros = [4, 3, 8, 12, 6, 10, 14, 3, 6]
# Se solicita:
# a) Eliminar el ´ultimo elemento de la lista
# b) Agregar en la primera posici´on el n´umero 2
# c) Eliminar los n´umeros duplicados de la lista
# d) Obtener la media y la mediana de la lista

numeros = [4, 3, 8, 12, 6, 10, 14, 3, 6]

# a) Eliminar el ´ultimo elemento de la lista
print(numeros)
print(f"Los numeros eliminado es el: {numeros.pop(8)}")
print(numeros)


# b) Agregar en la primera posici´on el n´umero 2

numeros.insert(0, 2)
print(numeros)

# c) Eliminar los n´umeros duplicados de la lista

numeros = list(set(numeros))
print(numeros)

# d) Obtener la media y la mediana de la lista

media = sum(numeros) / len(numeros)
print(media)

#ahora sacamos la mediana

numeros.sort()
print(numeros)

if len(numeros) % 2 == 0:
    mediana = (numeros[len(numeros) // 2] + numeros[len(numeros) // 2 - 1]) / 2
else:
    mediana = numeros[len(numeros) // 2]

print(mediana)