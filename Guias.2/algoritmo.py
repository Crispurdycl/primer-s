numero = int(input("Ingrese un numero: "))        
impar = (numero*(numero-1))+1
acum = 0

for i in range(numero, numero*3, 2):
    acum += impar
    if i == (numero-1):
        break 
    impar += 2 
    print(impar-2)

print(f"El cubo de {numero} es: {acum}")