class Animal:
    def __init__(self, dna):
        self.dna = dna

    def procreate(self):
        print("Make babies!")


class Dog(Animal):
    def __init__(self, dna, fur):
        super().__init__(dna)
        self.fur = fur

    def bark(self):
        print("Bark bark!")


dog = Dog("TTGG", True)
dog.procreate()
dog.bark()
