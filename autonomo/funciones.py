def Suma (a, b):
    return a + b

while True:
    try:
        a = float(input("Ingrese un número: "))
        break
    except ValueError:
        print("No es un número válido")

while True:
    try:
        b = float(input("Ingresa otro número: "))
        break
    except ValueError:
        print("No es un número válido")

print(f"La suma de {a} y {b} es: {Suma(a, b)}")