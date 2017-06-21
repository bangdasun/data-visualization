"""
    Basic plot: line / scatter / histogram
    
        plt.plotfunc() => plt... aesthetics => plt.show()

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv("C://Users//Bangda//Desktop//iris.csv", index_col = 0)
iris.head()

### Scatter plot
pLength = iris['Petal.Length']
pWidth  = iris['Petal.Width']
plt.scatter(pLength, pWidth, c = 'b', alpha = 1./5)
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.title('Scatter plot of length and width of Petal')
plt.grid(True)
plt.show()
plt.clf()

### Histogram
n, bins, patches = plt.hist(pWidth, bins = 20, color = 'g', alpha = 0.75, normed = True) # convert to np.array if doesn't work
plt.xlabel('Petal width')
plt.title('Distribution of petal width')
plt.grid(True)
plt.show()
plt.clf()