import requests

response = requests.get ("https://api.pokemonbattle.me:9104/trainers")
print(response)

response = requests.get ('https://api.pokemonbattle.me:9104/trainers',
                         params= {'trainer_id' : 3650})
print(response.text)


