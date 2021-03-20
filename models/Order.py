
from datetime import datetime


class Order:
    def __init__(self, quantity, price, action, n):
        self.quantity = quantity
        self.price = price
        self.action = action
        self.status = "open"
        self.createdAt = datetime.now()
        self.number = n

    def isOpen(self):
        return self.status == "open"

    def isClosed(self):
        return not self.isOpen()

    def closeOrder(self):
        self.status = "closed"

    def getAction(self):
        return self.action

    def getTotal(self):
        return self.quantity * self.price

    def close(self):
        self.status = "closed"

    def __str__(self):
        if (self.action == "buy"):
            return "PLACED " + self.action.upper()+" ORDER #"+str(self.number) + "  " + str(self.quantity) + " units" + " at " + str(self.price) + " each (Total spent: " + str(self.getTotal()) +")"
        else:
            return "PLACED " + self.action.upper()+" ORDER #"+str(self.number) + "  " + str(self.quantity) + " crypto units" + " at " + str(self.price) + " each (Total sold: " + str(self.getTotal()) +")"