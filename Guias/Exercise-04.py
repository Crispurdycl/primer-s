# Elaborar un algoritmo que solicite al usuario su nombre y el nombre de otra
# persona. Luego, mostrar en pantalla un mensaje que indique si ambos nombres
# comienzan con la misma letra o si terminan con la misma letra, o si difieren tanto
# en la letra inicial como en la final. Por ejemplo, si los nombres ingresados son
# Belinda y Beatriz, se mostrar´a un mensaje que indique que ambos nombres comienzan con la misma letra. Si los nombres son Leonardo y Gonzalo, se mostrar´a
# un mensaje que indique que ambos nombres terminan con la misma letra.

while True:
    name = input("Ingrese su nombre: ")
    if name == "" or name.isnumeric() == True:
        print("El nombre no es valido")
    else:
        break

while True:
    name2 = input("Ingrese el nombre de otra persona: ")
    if name2 == "" or name2.isnumeric() == True:
        print("El nombre no es valido")
    else:
        break
    