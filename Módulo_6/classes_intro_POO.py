
#CLASSES
class computador(object):
    def __init__(self,marca,memoria,placa):
        self.marca = marca
        self.memoria = memoria
        self.placa = placa
    def marcas(self):
        print(f'Seu computador é da marca {self.marca}')
    
    def memorias(self):
        print(f'Seu computador possui {self.memoria} Gb de memoria ram')

    
    def placas(self):
        print(f'Seu computador possui uma placa de video: {self.placa}')


marca = input('Digite a marca do seu computador: \n')
memoria = input('Digite a quantidade de memoria ram do seu computador: \n')
placa = input('Digite a placa de video do seu computador: \n')

computador=computador(marca, memoria, placa)
computador.marcas()
computador.memorias()
computador.placas()

