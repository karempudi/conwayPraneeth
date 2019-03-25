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

    return mat

def plotGameState(mat, plotNumber):
    """ Function to call plotting of the game statue using matplot lib """
    plt.figure(plotNumber)
    plt.imshow(mat[1:-1, 1:-1])
    plt.show()
    return None

def calculateNeighbours(mat):
    """ Function to calculate the neighbour matrix of the central grid, excluding the border of the grid"""
    N = mat[:-2, :-2] + mat[:-2, 1:-1] + mat[:-2, 2:] + mat[1:-1, :-2] + mat[1:-1, 2:] + mat[2:, :-2] + mat[2:, 1:-1] + mat[2:, 2:]
    return (N == 2) | (N == 3)

def updateGame(mat):
    mat[1:-1, 1:-1] = calculateNeighbours(mat)

if __name__ == "__main__":
    board = initializeCross(32)
    plotGameState(board, 100)
    updateGame(board)
    plotGameState(board, 100)


    


    



