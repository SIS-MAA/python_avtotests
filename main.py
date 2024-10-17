import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '54b465bd7fa146a517ee1709065242e2'
HEADER = {
    'Content-Type' : 'application/json',
    'trainer_token' : TOKEN
    }

create_pokemons = { 
    "name": "Бульбазавр",
    "photo_id": 2
}

delete_pokemons = {
    "pokemon_id": "91466"
}

new_name = {
    "pokemon_id": "98105",
    "name": "Serhio",
    "photo_id": 2
}

add_pok = {
    "pokemon_id": "98105"
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = create_pokemons)
print(response.text)

#response = requests.post(url = f'{URL}/pokemons/knockout', headers = HEADER, json = delete_pokemons)
#print(response.text)

response = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = new_name)
print(response.text)

response = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = add_pok)
print(response.text)

