class Shape:
    def __init__(self, name):
        self.name = name

    def calculate_area(self):
        raise NotImplementedError("Metoda calculate_area() musi byť implementovna v potomcich.")