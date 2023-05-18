# Elaborar un algoritmo que permita al usuario ingresar un mes y arroje la estaci´on
# correspondiente a ese mes: verano, oto˜no, invierno o primavera.



verano = ["enero", "Enero", "Febrero", "febrero", "diciembre", "Diciembre"]
otoño = ["Marzo", "marzo", "Abril", "abril", "Mayo", "mayo"]
invierno = ["Junio", "junio", "Julio", "julio", "Agosto", "agosto"]
primavera = ["Septiembre", "septiembre", "Octubre", "octubre", "Noviembre", "noviembre"]
#siuu
while True:
    mes = input("Ingrese un mes: ")
    if mes == "" or mes.isnumeric() == True:
        print("El mes no es valido")
    else:
        break

if mes in verano:
    print(f"{mes} es un mes de verano")
elif mes in otoño:
    print(f"{mes} es un mes de otoño")
elif mes in invierno:
    print(f"{mes} es un mes de invierno")
elif mes in primavera:
    print(f"{mes} es un mes de primavera")
else:
    print("El mes no es valido")