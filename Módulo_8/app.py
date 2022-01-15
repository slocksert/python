import os

#print(os.listdir())
caminho1=os.path.join(os.getcwd() + os.sep + 'Módulo_8'+ os.sep +'desafio arquivos' + os.sep + 'desafio texto' + os.sep + 'desafio texto1.txt')
caminho2=os.path.join(os.getcwd() + os.sep + 'Módulo_8'+ os.sep +'desafio arquivos' + os.sep + 'desafio texto' + os.sep + 'desafio texto2.txt')
caminho3=os.path.join(os.getcwd() + os.sep + 'Módulo_8'+ os.sep +'desafio arquivos' + os.sep + 'desafio texto' + os.sep + 'desafio texto3.txt')

print(caminho1)
print(caminho2)
print(caminho3)

chdir = os.chdir(os.getcwd() + os.sep + 'Módulo_8'+ os.sep +'desafio arquivos' + os.sep + 'desafio texto')
chdir2 = os.chdir('..')
chdir3 = os.chdir('..')
print(os.getcwd())