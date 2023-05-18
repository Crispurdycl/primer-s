# Existen dos grupos de estudiantes de la carrera de Programaci´on que formaron
# sus grupos para elaborar el Laboratorio N°3. Los grupos son los siguientes:

# Grupo 1
# Marcos
# Gabriela
# Benjamin
# Matias

# Grupo 2
# Marcos
# Nicol´as
# Diego
# Matias

# Se necesita saber si en ambos grupos tienen alg´un estudiante en com´un y, en caso
# de que as´ı sea, imprimir los nombres de esos estudiantes. Todo esto utilizando
# Sets.

# creamos nuestro set con los nombres de los grupos

grupo1 = {"Marcos", "Gabriela", "Benjamin", "Matias"}
grupo2 = {"Marcos", "Nicolas", "Diego", "Matias"}

# ahora hay que ver si alguno se repite

print(f"Los estudiantes que se repiten son: {grupo1.intersection(grupo2)} \n")