class BankAccount:
    def __init__(self, deposit=0):
        self._balance = deposit

    def deposit(self, money):
        self._balance += money


    def withraw(self, money):
        if self._balance >= money:
            self._balance -= money
            return True
        return money

    def __str__(self):
        return f"Na učtu je penez {self._balance}"
