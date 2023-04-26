def suma (a, b):
    return a + b
def resta (a, b):
    return a - b
def multiplicacion (a, b):
    return a * b
def division (a, b):
    return a / b

print("Bienvenido a la calculadora de Cristian")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
print("5. Salir")

while True:
    eleccion = input("¿Que operacion quieres realizar?:\n ")
    if eleccion in ("1", "2", "3", "4"):
        num1 = float(input("Primer numero:\n "))
        num2 = float(input("Segundo numero:\n "))
        if eleccion == "1":
            print(num1, "+", num2, "=", suma(num1, num2))
        elif eleccion == "2":
            print(num1, "-", num2, "=", resta(num1, num2))
        elif eleccion == "3":
            print(num1, "*", num2, "=", multiplicacion(num1, num2))
        elif eleccion == "4":
            print(num1, "/", num2, "=", division(num1, num2))
        break
    elif eleccion == "5":
        print("Hasta luego")
        break
    else:
        print("Opcion no valida")