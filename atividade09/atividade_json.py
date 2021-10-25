import json
from pathlib import Path

carros = [
        {"Marca": "Nissan", "Preço": 45.000, "Cor": "Azul"},
        {"Marca": "Ford", "Preço": 75.000, "Cor": "Verde"},
        {"Marca": "BMW", "Preço": 117.000, "Cor": "Amarelo"}
]

carros_json = json.dumps(carros)
Path('carros.json').write_text(carros_json)

arquivo__carros_json = Path('carros.json').read_text()
arquivo_json = json.loads(arquivo__carros_json )
print(arquivo_json [0]['Marca'])
