
from turtle import Turtle
import sys

#Inicializar uma turtle
t = Turtle()

#Definir velocidade
t.speed(1)

def obter_distancia():
    distancia = int(input("Quantos pixels você quer andar?\n"))
    return distancia

def obter_lado():
    lado = input("Agora, para qual lado você quer virar? d:Direita e:Esquerda ou n:Não rotacionar\n")
    if lado == 'd':
        direita(t)
    elif lado == 'e':
        esquerda(t)

def direita(turle):
    angulo = int(input("Quantos graus você quer rotacionar?\n"))
    t.right(angulo)

def esquerda(turle):
    angulo = int(input("Quantos graus você quer rotacionar?\n"))
    t.left(angulo)


try:
    while True:
        direção = input("Para qual direção devemos ir? f:frente ou t:trás\n")
        if direção == 'f':
            distancia = obter_distancia()
            obter_lado()
            t.forward(distancia)
        if direção == 't':
            distancia = obter_distancia()
            obter_lado()
            t.backward(distancia)
        play =input("Deseja continuar andando? s/n \n")
        if play == 's':
            continue
        else:
            print("Obrigado por jogar")
            break

except KeyboardInterrupt:
    print("Programa fechado pelo user")
    sys.exit()

    