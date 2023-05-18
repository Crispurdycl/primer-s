#escribir un programa que permite capturar una cadena de caracteres e imprima un diccionario con la cantidad de apariciones de cada palabra que existen en la cafena
#por ejemplo: "que lindo dia que hace hoy"
#debera imprimir que: 2 lindo: 1 dia: 1 hace: 1 hoy: 1

cadena = input("ingresa una frase: ")

cadena_sep = cadena.split()

print(cadena_sep)

diccionario = {}

for i in cadena_sep:
    if i not in diccionario:
        count = cadena_sep.count(i)
        diccionario[i]=count

print(diccionario)