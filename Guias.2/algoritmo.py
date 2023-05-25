numero = int(input("Ingrese un numero: "))        
impar = (numero*(numero-1))+1
cum = 0

for i in range(numero, numero*3, 2):
    cum += impar
    if i == (numero-1):
        break 
    impar += 2
    print(impar-2, "+ ", end="" )

print("= ", cum , end="\n")

print(f"El cubo de {numero} es: {cum}")