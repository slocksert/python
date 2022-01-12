from operator import itemgetter

""" pessoas =[
    {'nome': 'John',
    'idade': 32,
    'nivel_acesso': 2},
    {'nome': 'Carol',
    'idade': 18,
    'nivel_acesso': 3},
    {'nome': 'Jhonatan',
    'idade': 21,
    'nivel_acesso': 1},
    {'nome': 'Dio',
    'idade': 15,
    'nivel_acesso': 3}
    ]
pessoas.sort(key=itemgetter('idade'))
print(pessoas)
     """

    # Ordene a lista de produtos abaixo pelo preço em ordem crescente
produtos = [
    {"nome": "Celular",
     "preco": 1500
     },
    {"nome": "Monitor",
     "preco": 500
     },
    {"nome": "Microfone",
     "preco": 300
     }
]
 #Ordene em ordem descrescente a lista de equipamento_filmagem por valor do equipamento
equipamento_filmagem = [
    ("Tripé", 300),
    ("Câmera", 1700),
    ("Iluminação", 200),
]
 #Ordene em ordem crescente a cotacao_moedas com base no valor da moeda
 
cotacao_moedas = [["usd", 5.25], ["brl", 1.56], ["eur", 6.47]]

#1
produtos.sort(key=itemgetter('preco'))
#print(f'Primeiro desafio: {produtos}')

#2
equipamento_filmagem.sort(key=itemgetter(1), reverse=True)
#print(f'Segundo desafio: {equipamento_filmagem}')

#3
cotacao_moedas.sort(key=itemgetter(1))
print(f'Terceiro desafio: {cotacao_moedas}')
