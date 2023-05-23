# Hacer un algoritmo que detecte si un número es
# par o impar, además si es un número primo y si es
# mayor o menor a 50. Para este ejercicio se solicita
# utilizar condicionales y bucles.
while True:
    try:
        num = int(input("Ingresa un numero: "))
        break
    except: ValueError()

if num % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")

if num > 50:
    print("El numero es mayor a 50")
else:
    print("El numero es menor a 50")

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print("El numero no es primo")
            break
    else:
        print("El numero es primo")
else:
    print("El numero no es primo")