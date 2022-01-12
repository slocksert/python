import random
import sys

#3. Você quer escolher aleatoriamente um número de 10-100 Imprima na tela um valor aleatório entre 10 e 100"

num = random.randint(10, 100)
input("Digite um número entre 10 e 100: \n")

try:
    if input == num:
        print("_"*50)
        print("\nParabéns você acertou com 1% de chance")
        print("_"*50)
    
    else:
        print("_"*50)
        print(f"\nVocê errou o número sorteado foi o {num}, tente novamente!")
        print("_"*50)
except KeyboardInterrupt:
    print("Sorteio cancelado!")
    sys.exit()