class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "Some generic sound"
    
    def __str__(self):
        return f"{self.name} is a {self.species}"
