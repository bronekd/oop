from .vehicle import Vehicle
import json
#rozšiřuje soubor vehicle dědičnost


class Car(Vehicle):
    def __init__(self, name, color):
        super().__init__(name) #novinka super je odkaz na předka dědím a zapamatovat si funkci super
        self.color = color

    def turn(self, direction):
        print(f"Odbočím do {direction}")
    def __str__(self):
        return f"name: {self.name}, color: {self.color}"

    def to_json(self):
        return json.dumps(self.__dict__)