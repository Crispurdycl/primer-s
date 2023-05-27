def fac (n):
    resultado = 1
    for i in range (1, n+1):
        resultado = resultado * i
    return resultado

num = int(input(f"Por favor, ingresa un número: "))
resultado = fac(num)
print(f"El factorial de {num} es {resultado}")