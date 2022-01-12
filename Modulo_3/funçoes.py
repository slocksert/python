#Desafio 1
""" def gerar_nome_completo(nome='Rildo',sobrenome='Silva'):
    print(f'Bem vindo {nome} {sobrenome}')

gerar_nome_completo() """

#Desafio 2
""" def calcular_valores(Preço, Quantidade=1):
    print(Preço*Quantidade)

calcular_valores(12,2) """
""" 
def exbir_preco(nome,preço):
    print(f'{nome} está no valor de {preço}')
 """
#Argumentos posicionais
""" exbir_preco('iphone',5000)
 """
#Argumentos nomeados
""" exbir_preco(nome='iphone',preço=5000) """

#Desafio 3
""" def gerar_objeto_personalizado(cor,*,altura,formato):
    print(f'{cor}, {altura}cm, {formato}')

gerar_objeto_personalizado('Branco',altura=2.1,formato='quadrangular') """

# *args
""" def somar(*valores, b):
    print(valores)

    for valor in valores:
        b += valor
    print(b)

somar(10,30,50,70,90, b=1)
 """

# Kwargs (keyword arguments)
""" def concatenar(**palavras):
    frase= ''
    for palavra in palavras.values():
        frase += palavra + ' '
    print(frase)

concatenar(a='rildo',b='silva') """


