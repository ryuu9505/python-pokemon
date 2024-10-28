class Pokemon:
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health

    def display_info(self):
        print(f"{self.name} (Lv. {self.level}) - Health: {self.health}")

if __name__ == "__main__":
    pikachu = Pokemon("pikachu", 3, 72.5)
    pikachu.display_info()