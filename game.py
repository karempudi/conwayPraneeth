import numpy as np
import matplotlib.pyplot as plt

def initializeRandom(sizeOfGrid):
    """ Function for randomly initializing a grid of particular size """
    mat = np.random.randint(2, size = (sizeOfGrid + 2 , sizeOfGrid + 2))
    
    return mat

def initializeCross(sizeOfGrid):
    """ Initializing a cross to the game state at t = 0 """
    mat = np.zeros((sizeOfGrid + 2, sizeOfGrid + 2))
    mat[:, int((sizeOfGrid + 2)/2)] = True
    mat[int((sizeOfGrid + 2)/2) , :] = True

    return mat

def plotGameState(mat):
    """ Function to call plotting of the game statue using matplot lib """
    plt.figure()
    plt.imshow(mat[1:-1, 1:-1])
    plt.show()

def calculateNeighbours(mat):
    """ Function to calculate the neighbour matrix of the central grid, excluding the border of the grid"""
    N = mat[:-2, :-2] + mat[:-2, 1:-1] + mat[:-2, 2:] + mat[1:-1, :-2] + mat[1:-1, 2:] + mat[2:, :-2] + mat[2:, 1:-1] + mat[2:, 2:]
    return N


if __name__ == "__main__":
    board = initializeRandom(32)
    plotGameState(board)

    



