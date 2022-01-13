# Arquivo JSON
import json
from pathlib import Path

carros=[
    {'Marca': 'Nissan','Preço':45000,'Cor': 'Azul'},
    {'Marca': 'Ford','Preço':76000,'Cor': 'Azul'},
    {'Marca': 'BMW','Preço':90000,'Cor': 'Azul'},
]

carros_json = json.dumps(carros)
Path('carros.json').write_text(carros_json)

arquivo_carros_json=Path('carros.json').read_text()
arquivo_json=json.loads(arquivo_carros_json)
print(arquivo_json[0]['Marca' ])