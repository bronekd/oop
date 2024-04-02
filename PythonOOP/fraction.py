#zlomek
class Fraction:
    def __init__(self, nominator, denominator):
        self.nominator = nominator
        self.denominator = denominator

    def __str__(self): #vypisuji zlomek
        return (f"Zlomek: {self.nominator}/{self.denominator}")

    def __eq__(self, other): # porovnávám zlomek
        return self.nominator * other.denominator == self.denominator + other.nominator

    def __add__(self, other):
        common_denominator = self.denominator * other.denominator
        new_nominator = self.nominator * other.denominator + other.nominator * self.denominator
        return Fraction(new_nominator, common_denominator)





