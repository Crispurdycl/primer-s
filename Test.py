#comparando terminos numericos (ASCII)
print("COMPARANDO NUMEROS")

palabra = input("Ingrese una palabra: ")
for ch in palabra:
    print(ch, end=" ")

palabra2 = input("\nIngrese otra palabra: ")
for ch1 in palabra2:
    print("")
    print(ch1, end=" ")

if palabra == palabra2:
    print("")
    print("\nLas palabras son iguales")
else:
    print("\nLas palabras son diferentes")