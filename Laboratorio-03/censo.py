#guardamos la informacion de la tabla en un diccionario, luego imprimimos el diccionario por consola

Id_Region = [14,12]
Region = ["Los Ríos", "Magallanes"]
Habitantes = (18429, 1382291)
Superficie = (404432, 166533)

Problema = 18429 / 404432
#sumamos todos los diccionarios

diccionario = dict(zip(Id_Region, zip(Region, Habitantes, Superficie)))
print("Este es la suma de todos los diccionarios: ", diccionario, "\n")

#creamos una nueva clave al diccionario llamada "Densidad"
#la densidad poblacional se calcula de la siguiente forma: (Densidad = Habitantes/Superficie)
#solo debe tener 1 decimal

densidad = [round(Habitantes[0] / Superficie[0], 1), round(Habitantes[1] / Superficie[1], 1)]
diccionario["Densidad"] = densidad
diccionario = dict(zip(Id_Region, zip(Region, Habitantes, Superficie, densidad)))
print("Aqui agregamos la densidad de cada Region: ",diccionario,"\n")

#agregamos otra clave llamada "Capital", correspondiente a la capital de cada region

Capital = ["Valdivia", "Punta Arenas"]
diccionario["Capital"] = Capital
diccionario = dict(zip(Id_Region, zip(Region, Habitantes, Superficie, densidad, Capital)))
print("Aqui agregamos la capital de caga Region: ",diccionario,"\n")

#agregamos otra clave con el nombre "Comunas" la cual sera una lista de 3 comunas de cada region como minimo

Comunas = [["Río Bueno", "La Union", "Paillaco"], ["Cabo de hornos", "Porvenir", "Puerto Williams"]]
diccionario["Comunas"] = Comunas
diccionario = dict(zip(Id_Region, zip(Region, Habitantes, Superficie, densidad, Capital, Comunas)))
print("Aqui agregamos las comunas de cada Capital: ", diccionario, "\n")

#creamos una ultima clave llamada "Provincia" la cual almacenara el nombres de las provincias correspondiente a cada region

Provincia = [("Valdivia", "Ranco"), ("Magallanes", "Antartica Chilena", "Tierra del Fuego", "Última Esperanza")]
diccionario["Provincia"] = Provincia
diccionario = dict(zip(Id_Region, zip(Region, Habitantes, Superficie, densidad, Capital, Comunas, Provincia)))
print("Aqui agregamos la provincia de cada Region: ", diccionario)
print("Fin")