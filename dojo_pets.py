class Ninja:
    def __init__(self, first_name, last_name, pet_animal, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet_animal = pet_animal
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet_animal.play()
        return self

    def feed(self):
        self.pet_animal.eat()
        return self

    def bathe(self):
        self.pet_animal.noise()
        return self


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



goldfish = Pet('Goldie', 'fish', 'call, dive, jump')
jason = Ninja('Jason', 'Yang', goldfish, 'plankton,shrimp, worm', 'flake')


jason.feed().walk().bathe()
goldfish.display()