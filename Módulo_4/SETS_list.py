#SET
numeros=[2,2,5,8]
frutas = ['maça','uva','banana','maça','morango']

set_numeros = set(numeros)
print(set_numeros)
set_frutas = set(frutas)
print(set_frutas)

set_numeros.add(10)
print(set_numeros)

print(set_numeros.symmetric_difference(set_frutas))

print(set_numeros.intersection(set_frutas))