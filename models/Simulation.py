from algorithms.Algorithm import Algorithm

from pydoc import locate

class Simulation:
    def __init__(self, wallet, algorithm = "Algorithm", startingBalance = 100, historical = "USDT-TEST-H.txt"):
        print("Loading Simulation Data...")
        files = open("historical/"+historical)
        data = []
        for l in files:
            data.append(float(l.replace("\n","")))
        self.historical = data[::-1]
        self.wallet = wallet
        self.startingBalance = 100
        self.orderBook = []
        self.lastPrice = self.historical.pop()
        module_ = locate('models.algorithms.'+algorithm)
        class_ = getattr(module_, algorithm)
        self.algorithm = class_(self)


    def tick(self):
        if (len(self.historical)>0):
            self.lastPrice = self.historical.pop()
            return self.lastPrice
        return None

    def isRunning(self):
        return len(self.historical)>0






