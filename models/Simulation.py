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
        self.lastPrice = 0

        self.orderCount = 1

    def placeBuyOrder(self, quantity, unitPrice):
        order = Order(quantity, unitPrice, "buy", self.orderCount)
        if (self.availableBalance >= order.getTotal()):
            self.orderCount+=1
            self.orderBook.append(order)
            self.availableBalance-= order.getTotal()
            self.lockedBalance+= order.getTotal()
            self.recalculateTotalBalance()
            print(order)
            return order
        else:
            raise Exception("Not enough balance to place buy order")

    def placeSellOrder(self, quantity, unitPrice):
        order = Order(quantity, unitPrice, "sell", self.orderCount)
        if (self.availableCryptoBalance >= quantity):
            self.orderCount+=1
            self.orderBook.append(order)
            self.availableCryptoBalance-= order.quantity
            self.lockedCryptoBalance+= order.quantity
            self.recalculateTotalBalance()
            print(order)
            return order
        else:
            raise Exception("Not enough crypto balance to place sell order")

    def tick(self):
        if (len(self.historical)>0):
            self.lastPrice = self.historical.pop()
            self.lastPrices.append(self.lastPrice)
            return self.lastPrice
        return None

    def processOrderBook(self):
        for buyOrder in list(filter(lambda x: x.getAction()=="buy" and x.isOpen(), self.orderBook)):
            if buyOrder.price >= self.lastPrice:

                self.lockedBalance-= buyOrder.getTotal()
                self.availableCryptoBalance+= buyOrder.quantity
                self.recalculateTotalBalance()

                print("BUY ORDER #"+str(buyOrder.number) + " CLOSED SUCCESSFULLY, EARNED " + str(buyOrder.quantity) + " Current price: " + str(self.lastPrices[-1]))
                print("Total value: " + str(self.totalSimulationValue()))
                buyOrder.close()
        for sellOrder in list(filter(lambda x: x.getAction()=="sell" and x.isOpen(), self.orderBook)):
            if sellOrder.price <= self.lastPrice:
                self.lockedCryptoBalance-= sellOrder.quantity
                self.availableBalance+= sellOrder.getTotal()
                self.recalculateTotalBalance()
                print("SELL ORDER FULLFILLED SUCCESSFULLY, EARNED " + str(sellOrder.getTotal()) + " USD " + " Current price: " + str(self.lastPrices[-1]))
                print("Total value: " + str(self.totalSimulationValue()))
                sellOrder.close()




    def recalculateTotalBalance(self):
        self.totalBalance = self.lockedBalance + self.availableBalance
        self.totalCryptoBalance = self.lockedCryptoBalance + self.availableCryptoBalance

    def totalSimulationValue(self):
        normalAmount = str(self.totalBalance + self.totalCryptoBalance * self.lastPrice)
        detailAmount = "( ["+str(self.availableBalance)+ " + " + str( abs(round(self.lockedBalance)))+"]" + " + [ ( " +str(self.availableCryptoBalance) + " + " + str(self.lockedCryptoBalance) + " ) * " + str(self.lastPrice) +" ) "
        return  normalAmount + " " + detailAmount


    def isRunning(self):
        return len(self.historical)>0






