# Definimos la funcion del algoritmo "Counting Sort"
def sort(lst):
   
   # Conseguimos el valor mínimo y máximo de la lista que nos dieron
   minVal = min(lst) 
   maxVal = max(lst) 

   # Creamos una lista auxiliar que mida de "min" - "max" y lo inicializamos en 0
   aux = []
   for x in range (0, maxVal + 1):
      aux.append(0)
   
   # Contamos cuantas veces aparece cada número
   for x in lst: 
      aux[x] += 1
   
   # Recorremos la lista y vamos acumulando los valores
   for index in range(0, maxVal + 1):
      if(index > 0):
         aux[index] += aux[index-1]
  
   # Creamos una lista auxiliar para la lista ya ordenada
   sortedList = []
   for x in lst:
      sortedList.append(0)

   for x in lst:
      sortedList[aux[x] - 1] = x
      aux[x] -= 1

   return sortedList
