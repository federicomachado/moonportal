from models.Wallet import Wallet
from models.Simulation import Simulation


sim = Simulation("Dummy")
while sim.isRunning():
    current = sim.tick()
    sim.algorithm.think()
print("END OF SIMULATION")
print("TOTAL: " + str(sim.totalSimulationValue()))
