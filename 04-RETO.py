nm = ()
ag = ()
ht = ()
wt = ()

p1 = ()
p2 = ()
p3 = ()

print("==================================================================================================\n")
print("----------==============[Bienvenido al programa de registro de pacientes]===============----------\n")
print("==================================================================================================")
while True:
    name = input("¿Cuál es el nombre del primer paciente? ") 
    if name == "" or name.isnumeric() == True:
        print("El nombre no es valido")
    else:
        nm += (name,)
        break

while True:
    age = int(input("¿Cuál es la edad del primer paciente? "))
    if age < 0 or age > 115:
        print("La edad no es valida")
    else:
        ag += (age,)
        break

while True:
    height = int(input("¿Cuál es tu estatura en cm del primer paciente? "))
    if height < 0 or height > 250:
        print("La estatura no es valida")
    else:
        ht += (height,)
        break

while True:
    weight = int(input("¿Cuál es el peso en kg del primer paciente? "))
    if weight < 0 or weight > 250:
        print("El peso no es valido")
    else:
        wt += (weight,)
        break

print("==================================================================================================")

while True:
    name = input("¿Cuál es el nombre del segundo paciente? ")
    if name == "" or name.isnumeric() == True:
        print("El nombre no es valido")
    else:
        nm += (name,)
        break

while True:
    age = int(input("¿Cuál es la edad del segundo paciente? "))
    if age < 0 or age > 115:
        print("La edad no es valida")
    else:
        ag += (age,)
        break

while True:
    height = int(input("¿Cuál es la estatura en cm del segundo paciente? "))
    if height < 0 or height > 250:
        print("La estatura no es valida")
    else:
        ht += (height,)
        break

while True:
    weight = int(input("¿Cuál es el peso en kg del segundo? "))
    if weight < 0 or weight > 250:
        print("El peso no es valido")
    else:
        wt += (weight,)
        break

print("==================================================================================================")

while True:
    name = input("¿Cuál es el nombre del tercer paciente? ")
    if name == "" or name.isnumeric() == True:
        print("El nombre no es valido")
    else:
        nm += (name,)
        break

while True:
    age = int(input("¿Cuál es la edad del tercer paciente? "))
    if age < 0 or age > 115:
        print("La edad no es valida")
    else:
        ag += (age,)
        break

while True:
    height = int(input("¿Cuál es la estatura en cm del tercer paciente? "))
    if height < 0 or height > 250:
        print("La estatura no es valida")
    else:
        ht += (height,)
        break

while True:
    weight = int(input("¿Cuál es el peso en kg del tercer paciente? "))
    if weight < 0 or weight > 250:
        print("El peso no es valido")
    else:
        wt += (weight,)
        break

print("==================================================================================================")

print("Los datos de los pacientes son: \n")
p1 += (nm[0], ag[0], ht[0], wt[0])
p2 += (nm[1], ag[1], ht[1], wt[1])
p3 += (nm[2], ag[2], ht[2], wt[2])

print("\n",p1,"\n",p2,"\n", p3)

input(print("Presione cualquier tecla para salir"))