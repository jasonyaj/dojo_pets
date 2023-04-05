import pets

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


goldfish = pets.Pet('Goldie', 'fish', 'call, dive, jump')
jason = Ninja('Jason', 'Yang', goldfish, 'plankton,shrimp, worm', 'flake')


jason.feed().walk().bathe()
goldfish.display()