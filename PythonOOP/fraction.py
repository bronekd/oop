from my_error import MyCustomError

#zlomek
class Fraction:
    def __init__(self, nominator, denominator):
        self.nominator = nominator
        self.denominator = denominator

    def __str__(self): #vypisuji zlomek
        return (f"Zlomek: {self.nominator}/{self.denominator}")

    def __eq__(self, other): # porovnávám zlomek
        return self.nominator * other.denominator == self.denominator + other.nominator

    def __add__(self, other): # plus
        common_denominator = self.denominator * other.denominator
        new_nominator = self.nominator * other.denominator + other.nominator * self.denominator
        return Fraction(new_nominator, common_denominator)

    def __iadd__(self, other): #se znaménkem += a jednu proměnou rovnou přepisuji. Učitel to má ve svém kodu Fraction
        if isinstance(other, Fraction):
            common_denominator = self.denominator * other.denominator
            self.nominator * other.denominator + other.nominator * self.denominator
            self.denominator = common_denominator
            return self
        #raise TypeError("Můj error: Unsupported operand type for +=: {} and {}") # starý ale funkční nový error vlastní
        raise MyCustomError("Můj error: Unsupported operand type for +=: {} and {}")




