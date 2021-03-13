from algorithms.Dummy import Dummy
from algorithms.Algorithm import Algorithm

class Simulation:
    def __init__(self, wallet, algorithm = "default", startingBalance = 100, historical = "USDT-TEST-H.txt"):
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
        if algorithm == "default":
            self.algorithm = Algorithm(self)
        else:
            # TO DO: Dynamic Load
            self.algorithm = Dummy(self)


    def tick(self):
        if (len(self.historical)>0):
            self.lastPrice = self.historical.pop()
            return self.lastPrice
        return None

    def isRunning(self):
        return len(self.historical)>0






