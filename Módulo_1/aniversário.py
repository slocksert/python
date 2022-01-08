from datetime import datetime

aniversário = datetime.strptime(input("Quando é o seu aniversário? (Utilize o formato ano/mês/dia) \n"), "%Y/%m/%d")
data = datetime.now()
prazo = aniversário - data
print(f"Só faltam {prazo.days} dias para o seu aniversário!")
print(data)