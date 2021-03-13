from Algorithm import Algorithm

class Dummy(Algorithm):
    def __init__(self, simulation):
        super(Dummy, self).__init__(simulation)

    def think(self):
        print("Inside Dummy")