def binomio(a, b):
    return (a^2 + 2*a*b + b^2)

while True:
    try:
        a = int(input("Selecciona un numero enetero superior a 0: "))
        if a > 0:
            break
        else:
            continue
    except ValueError:
        print("Ingrese caracteres validos...")

while True:
    try:
        b = int(input("Selecciona un numero enetero superior a 0: "))
        if b > 0:
            break
        else:
            continue
    except ValueError:
        print("Ingrese caracteres validos...")

print(f"Tu binonomio es {binomio(a,b)}")