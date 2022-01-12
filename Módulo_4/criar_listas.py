#Como podemos criar listas?
#criar listas usando loops e range()
numeros = []
for i in range(5):
    numeros.append(i)
print(numeros)
#Map
nomes=['Larissa','Rafael','Pedro','Joao']
def aprovar(nome):
    return nome + ' Aprovado'

print(list(map(aprovar, nomes)))