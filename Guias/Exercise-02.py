# Escribir un programa que pida al usuario ingresar dos palabras y las guarde en
# dos variables diferentes. Luego imprimir cuál palabra tiene más caracteres y cuál
# tiene menos caracteres.


while True:
    palabra1 = input("Ingrese una palabra: ")
    if palabra1 == "" or palabra1.isnumeric() == True:
        print("No es valido, ingresa otro valor")
    else:
        break

while True:
    palabra2 = input("Ingrese otra palabra: ")
    if palabra2 == "" or palabra2.isnumeric() == True:
        print("No es valido, ingresa otro valor")
    else:
        break

if len(palabra1) > len(palabra2):
        print(f"La palabra \"{palabra1}\" tiene mas caracteres que la palabra \"{palabra2}\"")
elif len(palabra1) < len(palabra2):
       print(f"La palabra \"{palabra2}\" tiene mas caracteres que la palabra \"{palabra1}\"")
else:
    print(f'La palabra "{palabra1}" tiene la misma cantidad de caracteres que la palabra "{palabra2}"')