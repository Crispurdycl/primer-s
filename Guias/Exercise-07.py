# Crear una lista con nombres de 5 trabajadores y otra lista con las edades de
# estos 5 trabajadores, Se solicita relacionar ambas listas en una sola estructura.
# La salida puede ser en tuplas o en un diccionario.

nombres = ["Cristian", "Franco", "Matias", "Boris", "Lorena"]
edades = [18, 18, 28, 18, 19]

# ahora imprimos los nombres con sus respectivas edades

# print(f"El nombre {nombres[0]} tiene {edades[0]} años")
# print(f"El nombre {nombres[1]} tiene {edades[1]} años")
# print(f"El nombre {nombres[2]} tiene {edades[2]} años")
# print(f"El nombre {nombres[3]} tiene {edades[3]} años")
# print(f"El nombre {nombres[4]} tiene {edades[4]} años")

#ahora lo imprimos con un for
for nombre, edad in zip(nombres, edades):
    print(f"El nombre {nombre} tiene {edad} años")