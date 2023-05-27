# 1. Realizar un algoritmo que indique el número menor y el número mayor entre tres
# enteros leidos por consola. Solo se deben ingresar números enteros.

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

print(f"El numero menor es: {min(num1, num2, num3)}")
print(f"El numero mayor es: {max(num1, num2, num3)}")