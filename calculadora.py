def Suma (a, b):
    return a + b
def Resta (a, b):
    return a - b
def Multiplicacion (a, b):
    return a * b
def Division (a, b):
    return a / b

print("Bienvenido a la calculadora de Cristian")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
print("5. Salir")

while True:
    opcion = input("Seleccione una opcio('1', '2', '3', '4'):n: ")
     if opcion in 
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        if opcion == '1':
            print(num1, "+", num2, "=", Suma(num1, num2))
        elif opcion == '2':
            print(num1, "-", num2, "=", Resta(num1, num2))
        elif opcion == '3':
            print(num1, "*", num2, "=", Multiplicacion(num1, num2))
        elif opcion == '4':
            print(num1, "/", num2, "=", Division(num1, num2))
        break
    else:
        print("Opcion invalida, intente de nuevo")