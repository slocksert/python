nomes=['Larissa','Rafael','Pedro','Joao']

def filtrar(pessoa):
    if pessoa=='Joao':
       return True
    else:
        return False

print(list(filter(filtrar, nomes)))

vagas=[
    ['vaga 1', 1200],
    ['vaga 2', 2550],
    ['vaga 3', 5000]
]
def salario(vaga):
    if vaga[1] > 2500:
        return True
    else:
        return False

print(list(filter(salario, vagas)))