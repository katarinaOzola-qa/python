import requests
token = ''


response = requests.post ('https://api.pokemonbattle.me:9104/pokemons' ,
           json={   
           "name": "Qatarrr",
           "photo": "https://dolnikov.ru/pokemons/albums/005.png"
           },
           headers = {'Content-Type': 'application/json',
           'trainer_token': token})
print(response.text)



response = requests.put ('https://api.pokemonbattle.me:9104/pokemons' ,
           json={   
           "pokemon_id": "20763",
           "name": "JeanPOKY",
           "photo": "https://dolnikov.ru/pokemons/albums/005.png"
           },
           headers = {'Content-Type': 'application/json',
           'trainer_token': token})
print(response.text)



response = requests.post ('https://api.pokemonbattle.me:9104/trainers/add_pokeball' ,
           json={   
           "pokemon_id": "20763",
           },
           headers = {'Content-Type': 'application/json',
           'trainer_token': token})
print (response.text)

