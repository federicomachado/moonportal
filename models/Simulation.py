from algorithms.Algorithm import Algorithm
from Order import Order

from pydoc import locate

class Simulation:
    def __init__(self, algorithm = "Algorithm", startingBalance = 100, historical = "USDT-TEST-H.txt"):
        print("Loading Simulation Data...")
        files = open("historical/"+historical)
        data = []
        for l in files:
            data.append(float(l.replace("\n","")))
        self.historical = data[::-1]

        self.totalBalance = 100
        self.availableBalance = self.totalBalance
        self.lockedBalance = 0

        self.totalCryptoBalance = 0
        self.availableCryptoBalance = 0
        self.lockedCryptoBalance = 0

        self.orderBook = []
        module_ = locate('models.algorithms.'+algorithm)
        class_ = getattr(module_, algorithm)
        self.algorithm = class_(self)
        self.lastPrices = []

    def placeBuyOrder(self, quantity, unitPrice):
        order = Order(quantity, unitPrice, "buy")
        if (self.availableBalance >= order.getTotal()):
            self.orderBook.append(order)
            self.availableBalance-= order.getTotal()
            self.lockedBalance+= order.getTotal()
            self.recalculateTotalBalance()
            print(order)
            return order
        else:
            raise Exception("Not enough balance to place buy order")


    def tick(self):
        if (len(self.historical)>0):
            self.lastPrice = self.historical.pop()
            self.lastPrices.append(self.lastPrice)

            self.processOrderBook()

            return self.lastPrice
        return None

    def processOrderBook(self):
        for buyOrder in list(filter(lambda x: x.getAction()=="buy" and x.isOpen(), self.orderBook)):
            if buyOrder.price <= self.lastPrice:

                self.lockedBalance-= buyOrder.getTotal()
                self.availableCryptoBalance+= buyOrder.quantity
                self.recalculateTotalBalance()

                print("BUY ORDER CLOSED SUCCESSFULLY, EARNED " + str(buyOrder.quantity) + " Crypto ")
                print("Total value: " + str(self.totalSimulationValue()))
                buyOrder.close()




    def recalculateTotalBalance(self):
        self.totalBalance = self.lockedBalance + self.availableBalance
        self.totalCryptoBalance = self.lockedCryptoBalance + self.availableCryptoBalance

    def totalSimulationValue(self):
        return self.totalBalance + self.totalCryptoBalance * self.lastPrice


    def isRunning(self):
        return len(self.historical)>0






