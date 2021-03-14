class Algorithm(object):
    def __init__(self, simulation):
        self.simulation = simulation

    def getLastPrice(self):
        return self.simulation.lastPrice

    def getLastPrices(self, n = 10, step = 1):
        res = []
        for i in range(0, len(self.simulation.lastPrices), step):
            if len(res) < n:
                res.append(self.simulation.lastPrices[::-1][i])
        return res

    def getWalletBalance(self):
        return self.simulation.wallet.balance

    ## Balance for Base Currency
    def getTotalBalance(self):
        return self.simulation.totalBalance

    def getAvailableBalance(self):
        return self.simulation.availableBalance

    def getLockedBalance(self):
        return self.simulation.lockedBalance

    def hasEnoughBalance(self, price, quantity):
        return self.getAvailableBalance() >= price*quantity



    def getOrderBook(self):
        return self.simulation.orderBook

    def placeBuyOrder(self, quantity, unitPrice):
        return self.simulation.placeBuyOrder(quantity, unitPrice)

    def placeSellOrder(self, quantity, unitPrice):
        return self.simulation.placeSellOrder(quantity, unitPrice)

    def getOpenOrders(self):
        return list(filter( lambda x: x.isOpen(), self.getOrderBook))[::-1]

    def getOpenBuyOrders(self):
        return self._getOpenOrdersDefault("buy")

    def getOpenSellOrders(self):
        return self._getOpenOrdersDefault("sell")

    def getClosedOrders(self):
        return list(filter( lambda x: x.isClosed(), self.getOrderBook))[::-1]





    def think(self):
        print("Seeing last price")
        print(self.getLastPrice())


    def _getOpenOrdersDefault(self, action):
        return list(filter( lambda x: x.getAction() == action, self.getOpenOrders))
