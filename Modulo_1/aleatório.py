import random

#Desafios Random 
#1. Você quer simular a opção de jogar uma moeda e resultar em cara ou coroa 
#jogue as opções dentro de uma variável e depois crie um programa que imprimir "cara" ou "coroa" na tela 

opções = ["Cara","Coroa"]
input("Qual você quer? Cara ou Coroa?\n")
print("_"*50)
resultado = random.choice(opções)

if input:
    print(f"\nCaiu {resultado}!".upper()) 
    
