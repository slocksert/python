import random
from datetime import datetime

print("---------- Olá, bem-vindo à nossa empresa ----------")
nome = input("\nDigite o seu nome: \n")
idade = input("\nDigite sua idade: \n")
aniver = datetime.strptime(input("\nDigite sua data de aniversário: \n"), '%d/%m/%Y')
hora_de_cadastro = datetime.now().strftime("%d/%m/%Y")
cartoes = ['R$50,00','R$250,00','R$120,00']
resultado_sorteio = random.choice(cartoes)

print("_"*50)
print(f"\nOlá {nome}, seu registro foi concluído no dia {hora_de_cadastro}.\nParabéns, houve um sorteio e você ganhou um cartão de compras no valor de {resultado_sorteio}.")
print("_"*50)