

class Wallet:
    def __init__(self, name, currency = "BTC", balance = 0):
        self.name = name
        self.currency = currency
        self.balance = balance
        self.transactions = []

    def __str__(self):
        return self.name + " ("+self.currency+") " + str(self.balance)

    def addBalance(self, balance):
        self.balance+=balance
        return self.balance

    def substractBalance(self, balance):
        return self.addBalance(-balance)

