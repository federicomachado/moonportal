from models.Wallet import Wallet

x = Wallet("Test Wallet", "DOGE", 0)
x.addBalance(5000)
print(x)