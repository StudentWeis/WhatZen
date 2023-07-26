import numpy as np
import matplotlib.pyplot as plt

magicMat = np.ones((10,10,10),dtype=np.int8)

ax = plt.matshow(magicMat)
plt.colorbar(ax.colorbar, fraction=0.025)
plt.title("matrix X")
plt.show()
