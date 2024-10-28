class Pokemon:
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health

    def display_info(self):
        print(f"{self.name} (Lv. {self.level}) - Health: {self.health}")

    def attack(self):
        print(f"{self.name} uses a basic attack!")


class ElectricPokemon(Pokemon):
    def attack(self):
        print(f"{self.name} uses Thunderbolt!")


class WaterPokemon(Pokemon):
    def attack(self):
        print(f"{self.name} uses Water Gun!")


if __name__ == "__main__":
    pikachu = ElectricPokemon("pikachu", 3, 72.5)
    squirtle = WaterPokemon("squirtle", 3, 80.0)

    pikachu.display_info()
    squirtle.display_info()

    pikachu.attack()
    squirtle.attack()


