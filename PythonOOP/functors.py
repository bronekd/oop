# nová věc Functors
#mám objekt který má metodu a dostávám coins nová megicmetoda __call__
# funktor je fce s vnitřním stavem a podobá se clousers.

class WalletFunctor:
    def __init__(self, startCoins=100):
        self.__startCoins = startCoins

    def __call__(self, coins=0):
        return self.__startCoins + coins

    def __str__(self):
        return f'coins: {self.__startCoins}'

w = WalletFunctor(50)

print(w, end=".....")
print(w())
print(w(28))







