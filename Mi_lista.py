print("Ejemplo de listas")
arcoiris=["Rosa", "Rosa Pastel", "Blanco"]

print(arcoiris)
longitud=len(arcoiris)
print("Elementos que contiene la lista de arcoiris:", longitud)
print(f"Elementos que contiene la lista arcoiris v2{longitud}")
print(" Accediendo a un elemento de la lista: ")
print(arcoiris[1])
print(f"Elemento en la posicion 0 es: {arcoiris[0]}")
print(f"El primer color del arcoiris es: ", arcoiris[0])
print("Agrega un elemento de la lista")
print(arcoiris)
arcoiris.append("Morado")
print(arcoiris)
print("Lista de los elementos de la lista de ciclo for: ")
for ronquillo in arcoiris:
    print(ronquillo) 