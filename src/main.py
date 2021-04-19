import countingSort

# Pedimos los números al usuario y los convertimos a un arreglo
lst = input("Ingresa los números, separados por un espacio: ").split()

# Convertimos el arreglo de strings a un arreglo de ints
lst = [int(i) for i in lst]

# Imprimimos el resultado ordenado
print("La lista ordenada es:")
print(countingSort.sort(lst))
