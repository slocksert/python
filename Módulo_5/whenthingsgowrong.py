#Exceções



try:
    valor = int(input('Digite um valor em dolares: \n'))
    print(valor*5.53)
except:
    print('Favor digitar apenas números')

internet=None
try:
    print('Fazendo conexão com a ' + internet)

except TypeError as erro:
    print('Não há conexão com a internet')
finally:
    print('Desfazendo a compra!')