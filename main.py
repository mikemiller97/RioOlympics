import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

#prepare data
linear_data = np.array([1, 4, 2 , 5])

#plot figure
fig = plt.figure()
plt.plot(linear_data, '-o')

#save file
fig.savefig('line.png')

