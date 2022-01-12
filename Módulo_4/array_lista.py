#Armazenar itens do mesmo tipo
from array import array

numeros = array('i',[1,2,3,4,5,6,7,8]) 
numeros.append(9)
numeros.insert(1, 2)
numeros.pop(2)
numeros.remove(2)
del numeros[1]
print(numeros)