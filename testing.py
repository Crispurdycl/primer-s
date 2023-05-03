print("Bienvenido")
nota = int(input("introduzca la nota adquirida: \n"))
if (nota > 0 and nota <= 50):
    print("Usted ha suspendido")
else:
        if (nota > 51 and nota <= 65):
            print("Usted ha aprovado")
        else:
                if (nota > 65 and nota <= 85):
                    print("Usted es un estudiante notable")
                else:
                        if (nota > 85 and nota <= 100):
                            print("Usted es un estudiante sobresaliente")
                        else:
                            if (nota > 100 and nota <= 150):
                                print("Estudiante con matricula de honor")
                            else:
                                print("Nota no valida")