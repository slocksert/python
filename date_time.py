from datetime import datetime

hour = datetime.now()
response = input("Deseja saber as horas? Responda com Sim ou Não...\n                       ")

if response == ("Sim"):
    print(hour)
else:
    print("_" *50)
    print("Ok !! :D")
    print("_" *50)
