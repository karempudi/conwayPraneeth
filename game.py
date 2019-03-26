import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

def initializeRandom(sizeOfGrid):
    """ Function for randomly initializing a grid of particular size """
    mat = np.random.randint(2, size = (sizeOfGrid + 2 , sizeOfGrid + 2))
    
    return mat

def initializeCross(sizeOfGrid):
    """ Initializing a cross to the game state at t = 0 """
    mat = np.zeros((sizeOfGrid + 2, sizeOfGrid + 2))
    mat[:, int((sizeOfGrid + 2)/2)] = True
    mat[int((sizeOfGrid + 2)/2) , :] = True
    cleanBoundaries(mat)

    return mat

def iterateGameState(mat, numberOfIterations):
    """ Function to call plotting of the game state using matplot lib """
    plt.figure("Game")
    plt.ion()
    for i in range(numberOfIterations):
        plt.imshow(mat[1:-1, 1:-1])
        updateGame(mat)
        plt.pause(0.01)
    plt.show()

    return None

def calculateNeighbours(mat):
    """ Function to calculate the neighbour matrix of the central grid, excluding the border of the grid"""
    N = mat[:-2, :-2] + mat[:-2, 1:-1] + mat[:-2, 2:] + mat[1:-1, :-2] + mat[1:-1, 2:] + mat[2:, :-2] + mat[2:, 1:-1] + mat[2:, 2:]
    # N is about the size of the visual region
    return (N == 2) | (N == 3)

def updateGame(mat):
    mat[1:-1, 1:-1] = calculateNeighbours(mat)

def cleanBoundaries(mat):
    """ Setting the boundary of the board to zero after every iteration, incase if we need it"""
    mat[0, :] = 0
    mat[-1,:] = 0
    mat[:, 0] = 0
    mat[:, -1] = 0

if __name__ == "__main__":
    board = initializeCross(33)
    iterateGameState(board, 10)




    


    



