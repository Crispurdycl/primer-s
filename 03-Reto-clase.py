
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
            if (ICA[0] > 0 and ICA[0] < 50):
                print("La calidad del aire es buena")
                break
            elif (ICA[0] > 50 and ICA[0] <=100):
                print("La calidad del aire es moderada")
                break
            elif (ICA[0] > 100 and ICA[0] <=150):
                print("La calidad del aire es Dañina a la salud para grupos sensibles")
                break
            elif (ICA[0] > 150 and ICA[0] <=200):
                print("La calidad del aire es Dañina a la salud")
                break
            elif (ICA[0] > 200 and ICA[0] <=300):
                print("La calidad del aire es Muy dañina a la salud")
                break
            elif (ICA[0] > 300):
                print("La calidad del aire es peligrosa")
                break       
        elif eleccion == "2":
            print(f"El indice de calidad del aire de Temuco es: {ICA[1]}")
            if (ICA[1] > 0 and ICA[1] < 50):
                print("La calidad del aire es buena")
                break
            elif (ICA[1] > 50 and ICA[1] <=100):
                print("La calidad del aire es moderada")
                break
            elif (ICA[1] > 100 and ICA[1] <=150):
                print("La calidad del aire es Dañina a la salud para grupos sensibles")
                break
            elif (ICA[1] > 150 and ICA[1] <=200):
                print("La calidad del aire es Dañina a la salud")
                break
            elif (ICA[1] > 200 and ICA[1] <=300):
                print("La calidad del aire es Muy dañina a la salud")
                break
            elif (ICA[1] > 300):
                print("La calidad del aire es peligrosa")
                break
        elif eleccion == "3":
            print(f"El indice de calidad del aire de Osorno es: {ICA[2]}")
            if (ICA[2] > 0 and ICA[2] < 50):
                print("La calidad del aire es buena")
                break
            elif (ICA[2] > 50 and ICA[2] <=100):
                print("La calidad del aire es moderada")
                break
            elif (ICA[2] > 100 and ICA[2] <=150):
                print("La calidad del aire es Dañina a la salud para grupos sensibles")
                break
            elif (ICA[2] > 150 and ICA[2] <=200):
                print("La calidad del aire es Dañina a la salud")
                break
            elif (ICA[2] > 200 and ICA[2] <=300):
                print("La calidad del aire es Muy dañina a la salud")
                break
            elif (ICA[2] > 300):
                print("La calidad del aire es peligrosa")
                break
        elif eleccion == "4":
            print(f"El indice de calidad del aire de Punta Arenas es: {ICA[3]}") 
            if (ICA[3] > 0 and ICA[3] <= 50):
                print("La calidad del aire es buena")
                break
            elif (ICA[3] > 50 and ICA[3] <=100):
                print("La calidad del aire es moderada")
                break
            elif (ICA[3] > 100 and ICA[3] <=150):
                print("La calidad del aire es Dañina a la salud para grupos sensibles")
                break
            elif (ICA[3] > 150 and ICA[3] <=200):
                print("La calidad del aire es Dañina a la salud")
                break
            elif (ICA[3] > 200 and ICA[3] <=300):
                print("La calidad del aire es Muy dañina a la salud")
                break
            elif (ICA[3] > 300):
                print("La calidad del aire es peligrosa")
                break
        break