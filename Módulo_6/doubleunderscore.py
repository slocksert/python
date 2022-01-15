class Pessoa:
    def __init__(self,nome,habilidade1,habilidade2,habilidade3):
        self.nome = nome
        self.habilidade1 = habilidade1
        self.habilidade2 = habilidade2
        self.habilidade3 = habilidade3
    
    def resultado(self):
        print(f'Seu nome de super-herói é {self.nome} e suas habilidades são:\n{self.habilidade1}\n{self.habilidade2}\n{self.habilidade3}')

nome = input('Digite seu nome de super-herói:\n')
habilidade1 = input('Digite sua primeira habilidade:\n')
habilidade2 = input('Digite sua segunda habilidade:\n')
habilidade3 = input('Digite sua terceira habilidade:\n')

pessoa=Pessoa(nome, habilidade1, habilidade2, habilidade3)
pessoa.resultado()