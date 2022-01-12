# Enumerate
# Desafio 1
frutas = ['Maça','Laranja','Morango','Limao']
for indice, fruta in enumerate(frutas,0):
    if indice == 3:
        print(f'{indice} {fruta} EM PROMOÇÃO')
    else:
        print(indice, fruta)