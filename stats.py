class CharacterStats:
    def __init__(self, characters):
        self.characters = characters
        self.stats = []

    def name(self, name, description=""):
        self.name.append({"name": name, "description": description})

    def health(self, amount, description=""):
        self.health.append({"Health": amount, "description": description})

    def strenght(self, amount, description=""):
        self.strenght.append({"Strenght": amount, "description": description})

    def defense(self, amount, description=""):
        self.defense.append({"Defense": amount, "description": description})

    def speed(self, amount, description=""):
        self.speed.append({"Speed": amount, "description": description})

    def luck(self, amount, description=""):
        self.luck.append({"Luck": amount, "description": description})

    def get_stats(self):
        return sum(info["info"] for info in self.stats)

    # def attack(self, amount):

    def __str__(self):
        output = self.characters.center(50, "-") + "\n"
        for info in self.stats:
            description = info["description"]
            amount = info["amount"].rjust(50 - len(description))
            output += f"{description}: {amount}\n"
        output += f"Name: {self.name}\nHealth: {self.health}\nStrenght: {self.strenght}\nDefense: {self.defense}\nSpeed: {self.speed}\nLuck: {self.luck}%"
        return output
