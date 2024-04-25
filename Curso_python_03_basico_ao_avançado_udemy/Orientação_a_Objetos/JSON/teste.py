import json
from pprint import pprint

ARQUIVO_JSON = """
{
    "title": "O Senhor dos Anéis: A sociédade do anel",
    "original_title": "The lord of the Rings: The Fellowship of the Rings",
    "is_movie": true,
    "year": 2015,
    "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
    "budget": null
}
"""

filme = json.loads(ARQUIVO_JSON)
print(filme['original_title'])
print(filme['characters'])
print(filme['characters'][1])