import numpy as np
import matplotlib.pyplot as plt

# the size of the screen
displaySize= 32

# Doing random initializations
mat = np.random.randint(2, size = (displaySize, displaySize), dtype=bool)

# Display the matrix using matplotlib
plt.imshow(mat)
plt.show()


