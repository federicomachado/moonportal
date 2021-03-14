from Algorithm import Algorithm

class Dummy(Algorithm):
    def __init__(self, simulation):
        super(Dummy, self).__init__(simulation)

    def think(self):
        if (self.hasEnoughBalance(2, 20)):
            self.placeBuyOrder(2, 20)
