
Ciudades = ["Santiago", "Temuco", "Osorno", "Punta Arenas"]
ICA = [134, 99, 245, 50]

minimo = ICA.index(min(ICA))
maximo = ICA.index(max(ICA))

print(f"La ciudad con mejor indice de calidad del aire es: {Ciudades[minimo]} con un indice de: {ICA[minimo]}\n")
print(f"La ciudad con peor indice de calidad del aire es: {Ciudades[maximo]} con un indice de: {ICA[maximo]}\n")
print(f"El indice de calidad del aire promedio es: {sum(ICA)/len(ICA):.2f}\n")

print("Seleccione la ciudad que desea consultar: \n")
print("1. Santiago\n")
print("2. Temuco\n")
print("3. Osorno\n")
print("4. Punta Arenas\n")

while True:
    eleccion = input(" ( 1 | 2 | 3 | 4 )\n ")
    if eleccion in ("1", "2", "3", "4"):
        if eleccion == "1":
            print(f"El indice de calidad del aire de Santiago es: {ICA[0]}")
            break
        elif eleccion == "2":
            print(f"El indice de calidad del aire de Temuco es: {ICA[1]}")
            break
        elif eleccion == "3":
            print(f"El indice de calidad del aire de Osorno es: {ICA[2]}")
            break
        elif eleccion == "4":
            print(f"El indice de calidad del aire de Punta Arenas es: {ICA[3]}")
            break
    else:
        print("Opcion no valida")
        break