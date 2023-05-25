print("Bienvenido")
nota = int(input("Ingresa el valor de tu nota: \n"))
if (nota > 0 and nota < 50):
    print("Haz suspendido el examen")
elif (nota > 50 and nota <= 65):
    print("Haz aprovado este examen")
elif (nota > 65 and nota <= 85):
    print("Usted es un estudiante notable")
elif (nota > 85 and nota <= 100):
    print("Usted es un estudiante sobresaliente")
elif (nota > 100):
    print("Estudiante con matricula de honor")