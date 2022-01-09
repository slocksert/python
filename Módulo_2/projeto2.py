from turtle import Turtle
import sys

#Inicializar uma turtle
t = Turtle()

#Definir velocidade
t.speed(1)

try:
    while True:
        direção = input("Para qual direção devemos ir? f:frente ou t:trás\n")
        if direção == 'f':
            distancia = int(input("Quantos pixels você quer andar?\n"))
            sentido = input("Agora, para qual lado você quer virar? d:direita ou e:esquerda\n")
            if sentido == 'd':
                angulo = int(input("Quanto para direita você quer rotacionar?\n"))
                t.right(angulo)
            elif sentido == 'e':
                angulo = int(input("Quanto para esquerda você quer rotacionar?\n"))
                t.left(angulo)
        if direção == 't':
            distancia = int(input("Quantos pixels você quer andar?\n"))
            sentido = input("Agora, para qual lado você quer virar? d:direita ou e:esquerda\n")
            if sentido == 'd':
                angulo = int(input("Quanto para direita você quer rotacionar?\n"))
                t.right(angulo)
            elif sentido == 'e':
                angulo = int(input("Quanto para esquerda você quer rotacionar?\n"))
                t.left(angulo)
        t.forward(distancia)
        play =input("Deseja continuar andando? s/n \n")
        if play == 's':
            continue
        else:
            print("Obrigado por jogar")
            break

except KeyboardInterrupt:
    print("Programa fechado pelo user")
    sys.exit()
