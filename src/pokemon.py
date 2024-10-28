from pokemon.base import Pokemon
from pokemon.types import ElectricPokemon, WaterPokemon
from pokemon.file_io import save_pokemon_to_file, load_pokemon_from_file, save_pokemon_to_json, load_pokemon_from_json


if __name__ == "__main__":
    pikachu = ElectricPokemon("pikachu", 3, 72.5)
    squirtle = WaterPokemon("squirtle", 3, 80.0)
    bulbasaur = Pokemon("bulbasaur", 3, 78.0)

    pokemon_list = [pikachu, squirtle, bulbasaur]

    for pokemon in pokemon_list:
        pokemon.display_info()
        pokemon.attack()
        print("-" * 20)

    pokemon_dict = {
        "pikachu": pikachu,
        "squirtle": squirtle,
        "bulbasaur": bulbasaur
    }

    name = "pikachu"
    if name in pokemon_dict:
        selected_pokemon = pokemon_dict[name]
        selected_pokemon.display_info()
        selected_pokemon.attack()

    save_pokemon_to_file(pikachu, "pokemon_data.txt")
    loaded_pokemon = load_pokemon_from_file("pokemon_data.txt")
    loaded_pokemon.display_info()

    save_pokemon_to_json(squirtle, "pokemon_data.json")
    loaded_pokemon = load_pokemon_from_json("pokemon_data.json")
    loaded_pokemon.display_info()