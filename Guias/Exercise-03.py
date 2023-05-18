# Desarrollar un programa que al momento de ingresar los lados de un triangulo
# (a, b y c) en consola, indique si es equilátero, isósceles o escaleno. También se
# solicita calcular el área utilizando la formula de Herón:

a = float(input("Ingrese el primer lado del triangulo: "))
b = float(input("Ingrese el segundo lado del triangulo: "))
c = float(input("Ingrese el tercer lado del triangulo: "))

if a == b and b == c:
    print("El triangulo es equilatero")
elif a == b or b == c or a == c:
    print("El triangulo es isosceles")
else:
    print("El triangulo es escaleno")

p = (a + b + c) / 2
area = (p*(p-a)*(p-b)*(p-c)) ** 0.5

print(f"El area del triangulo es: {area:.2f}")