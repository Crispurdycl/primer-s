"""ESTO ES UNA CALCULADORA"""

def Suma (a, b):
    return a + b
def Resta (a, b):
    return a - b
def Multiplicacion (a, b):
    return a * b
def Division (a, b):
    return a / b
def Potencia (a, b):
    return aEb
def Raiz (a):
    return a ** (1/2)

print("Seleccione una operacion\n")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
print("5. Potencia")
print("6. Raiz")

while True:
    eleccion = input(" ( 1 | 2 | 3 | 4 | 5 | 6 )\n ")
    if eleccion in ("1", "2", "3", "4", "5", "6"):
        if eleccion == "1":
            num1=float(input("Por favor ingresa tu PRIMER numero: "))
            num2=float(input("Por favor ingresa tu SEGUNDO numero: "))
            print(f"{num1} + {num2} =", Suma (num1, num2))
        elif eleccion == "2":
            num1=float(input("Por favor ingresa tu PRIMER numero: "))
            num2=float(input("Por favor ingresa tu SEGUNDO numero: "))
            print(f"{num1} - {num2} =", Resta (num1, num2))
        elif eleccion == "3":
            num1=float(input("Por favor ingresa tu PRIMER numero: "))
            num2=float(input("Por favor ingresa tu SEGUNDO numero: "))
            print(f"{num1} * {num2} =", Multiplicacion (num1, num2))
        elif eleccion == "4":
            num1=float(input("Por favor ingresa tu PRIMER numero: "))
            num2=float(input("Por favor ingresa tu SEGUNDO numero: "))
            print(f"{num1} / {num2} =", Division (num1, num2))
        elif eleccion == "5":
            num1=float(input("Por favor ingresa tu BASE: "))
            num2=float(input("Por favor ingresa tu EXPONENTE: "))
            print(f"{num1} ** {num2} =", Potencia (num1, num2))
        elif eleccion == "6":
            num1=float(input("Por favor ingresa tu numero: "))
            print(f"La raiz cuadrada de {num1} es", Raiz (num1))
            break