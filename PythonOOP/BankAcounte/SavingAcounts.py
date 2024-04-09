from .BankAcounts import *

class SavingsAccount(BankAccount):
    def __init__(self, bank_account, deposit = 0):
        """

        :param bank_account: je vstup typu BankAccount
        :param deposit:
        """
        super().__init__(bank_account.withraw(deposit) * 1.1)
        self.__bank_account = bank_account

    def deposit(self, money):
        """
        metoda vytáhne požadované zdroje z účtu jestli je to možné. popíšu co to dělá
        :param money: požadované množství peněz
        :return: jeslti se akce povedla
        """
        self._balance += money * 1.1