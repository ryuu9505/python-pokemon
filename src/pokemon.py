class Pokemon:
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health

    def display_info(self):
        print(f"{self.name} (Lv. {self.level}) - Health: {self.health}")

    def attack(self):
        print(f"{self.name} uses a basic attack!")


def save_pokemon_to_file(pokemon, filename):
    with open(filename, 'w') as file:
        file.write(f"{pokemon.name},{pokemon.level},{pokemon.health}\n")


def load_pokemon_from_file(filename):
    with open(filename, 'r') as file:
        line = file.readline().strip()
        name, level, health = line.split(',')
        return Pokemon(name, int(level), float(health))


class ElectricPokemon(Pokemon):
    def attack(self):
        print(f"{self.name} uses Thunderbolt!")


class WaterPokemon(Pokemon):
    def attack(self):
        print(f"{self.name} uses Water Gun!")


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
