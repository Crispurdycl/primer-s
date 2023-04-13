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
    return a ** b
def Raiz (a, b):
    return sqrt(a)

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
        num1=float(input("Por favor ingresa tu PRIMER numero: "))
        num2=float(input("Por favor ingresa tu SEGUNDO numero: "))

        if eleccion == "1":
            print(f"{num1} + {num2} =", Suma (num1, num2))
        elif eleccion == "2":
            print(f"{num1} - {num2} =", Resta (num1, num2))
        elif eleccion == "3":
            print(f"{num1} * {num2} =", Multiplicacion (num1, num2))
        elif eleccion == "4":
            print(f"{num1} / {num2} =", Division (num1, num2))
        elif eleccion == "5":
            print(f"{num1} ** {num2} =", Potencia (num1, num2))
        elif eleccion == "6":
            print(f"La raiz cuadrada es {num1}", Raiz (num1)) 
            break