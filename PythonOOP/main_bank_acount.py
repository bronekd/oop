from BankAcounte import *

b = BankAccount(100)
s = SavingsAccount(b, 50)

print(b)
print(s)

b.deposit(100)
s.deposit(200)

print(b)
print(s)