import ninja

class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks

        self.health = 100
        self.energy = 100

    def sleep(self):
        self.energy += 25

    def eat(self):
        self.health += 10
        self.energy += 5

    def play(self):
        self.health += 5

    def noise(self):
        noise = "bubble pop"
        print(noise)

    def display(self):
        health = self.health
        energy = self.energy
        print(self.health)
        print(self.energy)

