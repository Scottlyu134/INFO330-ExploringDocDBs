from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

separator = ''.join(['-' for _ in range(50)]) 
print(separator)

query = {"abilities": {'$regex': ".*Overgrow.*"}}
results_pokemon = pokemonColl.find(query)

for pokemon in results_pokemon:
    print(pokemon)