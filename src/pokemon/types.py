from .base import Pokemon


class ElectricPokemon(Pokemon):
    def attack(self):
        print(f"{self.name} uses Thunderbolt!")


class WaterPokemon(Pokemon):
    def attack(self):
        print(f"{self.name} uses Water Gun!")
