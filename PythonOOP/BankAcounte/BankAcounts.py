class BankAccount:
    counter = 0 #společný pro všechny účty

    def __init__(self, deposit=0):
        self._balance = deposit

    def deposit(self, money):
        self._balance += money

    @classmethod
    def add_counter(cls, num):
        cls.counter += num

    @classmethod
    def get_counter(cls):
        return cls.counter

    def withraw(self, money):
        if self._balance >= money:
            self._balance -= money
            return True
        return money

    def __str__(self):
        return f"Na učtu je penez {self._balance}"

    @staticmethod
    def sayGreatings():
        print("Nice to meet you")
        #statická metoda používám jen jednou vhodné pro kalkulačku