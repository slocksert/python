
from turtle import Turtle
import sys

#Inicializar uma turtle
t = Turtle()

#Definir velocidade
t.speed(1)

try:
    while True:
        direção=(input("Quer ir para trás ou para frente? f/t \n"))
        distancia=int(input("E Quantos pixels quer andar?\n"))
        sentido=input("Quer virar para qual lado? d/e/p \n")
        angulo=int(input("Quantos graus deseja rotacionar?\nPara não rotacionar utilize '0'\n"))
        

        if sentido == 'd':
            t.right(angulo)
            if direção == 'f':
                t.forward(distancia)
        elif sentido == 'e':
            t.left(angulo)
            if direção == 't':
                t.backward(distancia)
        play=input("Deseja continuar andando? s/n\n")
        if play == 's':
            continue
        elif play == 'n':
            break
        else:
            break

except KeyboardInterrupt:
    print("Programa fechado pelo user")
    sys.exit()

    