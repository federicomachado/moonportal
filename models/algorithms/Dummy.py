from Algorithm import Algorithm

class Dummy(Algorithm):
    def __init__(self, simulation):
        super(Dummy, self).__init__(simulation)

    def think(self):
        lastPrice = self.simulation.lastPrice
        if (self.hasEnoughBalance(2, lastPrice - lastPrice*0.10)):
            self.placeBuyOrder(2, lastPrice - lastPrice*0.10)
        if (self.hasEnoughCryptoBalance(2)):
            self.placeSellOrder(2, lastPrice*1.1)
