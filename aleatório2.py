import random
import sys

#2. Você quer fazer um sorteio entre 5 nomes em uma lista de nomes Crie uma lista de 5 nomes e sorteie um nome de dentro dessa lista e exiba na tela 

sorteio = ["Ana","Elizabeth","Henry","John","Sarney"]
resultado = random.choice(sorteio)
try:
    if input:
        print("E o(a) vencedor(a) é...")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(f"{resultado}!!!!!".upper())

except KeyboardInterrupt:
    print("Sorteio cancelado!")
    sys.exit()