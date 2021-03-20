from models.Wallet import Wallet
from models.Simulation import Simulation


sim = Simulation("Dummy", "USDT-TEST-H.txt")
print("")
print ("START OF SIMULATION")
print("TOTAL: " + str(sim.totalSimulationValue()))
print("*******************************************")
while sim.isRunning():
    current = sim.tick()
    sim.algorithm.think()
    sim.processOrderBook()
print("*******************************************")
print("END OF SIMULATION")
print("TOTAL: " + str(sim.totalSimulationValue()))
