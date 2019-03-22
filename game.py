import numpy as np
import matplotlib.pyplot as plt

def initialize_random(sizeOfGrid):
    """ Function for randomly initializing a grid of particular size """
    mat = np.random.randint(2, size = (sizeOfGrid, sizeOfGrid), dtype=bool)
    
    return mat

def plotGameState(mat):
    """ Function to call plotting of the game statue using matplot lib """
    plt.imshow(mat)
    plt.show()

def calculateNeighbours(mat):
    """ Function to calculate the neighbour matrix of the central grid, excluding the border of the grid"""

    return None
