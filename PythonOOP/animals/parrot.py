from animal import Animal
from walkable import Walkable
from flyable import Flayble

class Parrot(Animal, Walkable, Flayble):

    def walk(self):
        print("parrot walking")

    def fly(self):
        print("parrot flying")

