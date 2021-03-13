from Algorithm import Algorithm

class Greed(Algorithm):
    def __init__(self, simulation):
        super(Greed, self).__init__(simulation)

    def think(self):
        print("Inside Greed")