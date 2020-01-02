"""
Script to generate and run 2D Brownian walk (BrownianPath) and
plot it (BrownianSim).

"""

import numpy as np
import matplotlib.pyplot as plt

def BrownianPath(nsteps):
    dt = 1 / nsteps
    # Simulate increments of the BM setting:
    dw = np.random.randn(nsteps, 2) * np.power(dt, 0.5)
    # Simulate Wiener process:
    bPaths = np.cumsum(dw, axis=0)
    return bPaths


def BrownianSim(bPath):
    # Plot simulated paths:
    plt.plot(bPath[:, 0], bPath[:, 1])
    plt.plot(bPaths[0, 0], bPaths[0, 1], 'ko')
    plt.title("2D Brownian motion for " + bPath.shape[0] +" steps")
    plt.xticks([], [])
    plt.yticks([], [])
    plt.savefig("Brownian2D.png")


bPaths = BrownianPath(100)
BrownianSim(bPaths)