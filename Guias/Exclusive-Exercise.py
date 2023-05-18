#vamos a ingresar tres notas y sacar el promedio
#y vamos a crear una funcion que limpie la pantalla

def limpiar_pantalla():
    import os
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

while True:
    try:
        print(("=") * 40)
        nota1 = float(input("Ingrese la primera nota: "))
        print(limpiar_pantalla())
        if nota1 < 1 or nota1 > 7:
            print("No es valido, ingresa otro valor")
        else:
            break
    except ValueError:
        print("No es valido, ingresa otro valor")

while True:
    try:
        print(("=") * 40)
        nota2 = float(input("Ingrese la segunda nota: "))
        print(limpiar_pantalla())
        if nota2 < 1 or nota2 > 7:
            print("No es valido, ingresa otro valor")
        else:
            break
    except ValueError:
        print("No es valido, ingresa otro valor")

while True:
    try:
        print(("=") * 40)
        nota3 = float(input("Ingrese la tercera nota: "))
        print(limpiar_pantalla())
        if nota3 < 1 or nota3 > 7:
            print("No es valido, ingresa otro valor")
        else:
            break
    except ValueError:
        print("No es valido, ingresa otro valor")

promedio = (nota1 + nota2 + nota3) / 3
print(f"El promedio de tus notas es: {promedio:.2f}")