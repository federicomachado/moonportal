from models.Wallet import Wallet
from models.Simulation import Simulation


wallet = Wallet("Main Wallet")
sim = Simulation(wallet, "Dummy")
while sim.isRunning():
    current = sim.tick()
    sim.algorithm.think()
