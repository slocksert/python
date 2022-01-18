import os

""" with open('log.txt','w') as log:
    log.write('log.warning')

with open('log.txt','a') as log:
    log.write('\nTESTE1') """

lista =  ['teste1','teste2','teste3','teste4']
lista2 = ['teste1','teste2','teste3','teste4']
lista3 = ['teste1','teste2','teste3','teste4']

""" with open('teste.txt','w',newline=('')) as teste:
    for lista1 in lista:
            teste.write(lista1 + os.linesep)  """

""" with open('Frutas.txt','w',newline='') as frutas:
    for fruta in lista:
        frutas.write(fruta + os.linesep) """

""" with open('Frutas.txt','r') as frutas:
    for linha in frutas:
        print(linha) """

""" with open('Frutas.txt','a',newline='') as frutas:
    for listas2 in lista2:
        frutas.write(listas2 + os.linesep) """
    
""" with open('Top 5 linguagens.txt','w',newline='') as linguagens:
    for lingua in lista3:
        linguagens.write(lingua + os.linesep) """

arquivo = ['Jabuticaba','Melão','Jambo','Abacaxi']

for arquivos in arquivo:
    with open(f'{arquivos}','w') as pasta:
        pasta.write('')
        