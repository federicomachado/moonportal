class Algorithm(object):
    def __init__(self, simulation):
        self.simulation = simulation


    def getLastPrice(self):
        return self.simulation.lastPrice

    def getWallet(self):
        return self.simulation.wallet

    def getWalletBalance(self):
        pass

    def getCurrentBalance(self):
        pass

    def getOrderBook(self):
        return self.simulation.orderBook

    def placeBuyOrder(self):
        pass

    def placeSellOrder(self):
        pass

    def getOpenOrders(self):
        pass

    def getClosedOrders(self):
        pass

    def think(self):
        print("Seeing last price")
        print(self.getLastPrice())
