import json
from .base import Pokemon


def save_pokemon_to_file(pokemon, filename):
    with open(filename, 'w') as file:
        file.write(f"{pokemon.name},{pokemon.level},{pokemon.health}\n")


def load_pokemon_from_file(filename):
    with open(filename, 'r') as file:
        line = file.readline().strip()
        name, level, health = line.split(',')
        return Pokemon(name, int(level), float(health))


def save_pokemon_to_json(pokemon, filename):
    data = {
        "name": pokemon.name,
        "level": pokemon.level,
        "health": pokemon.health
    }
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_pokemon_from_json(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return Pokemon(data["name"], data["level"], data["health"])
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON. The file format might be incorrect.")
    except KeyError as e:
        print(f"Error: Missing key in JSON data - {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Attempted to load Pokémon data from JSON.")


