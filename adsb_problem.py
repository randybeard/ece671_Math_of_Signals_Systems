import numpy as np
import matplotlib.pyplot as plt

num_samples = 10000

# Download CSV file from the link provided
data = np.genfromtxt("adsb_data.csv", delimiter=",")
x = np.linspace(0, 5, num_samples)

# Plot data
plt.figure(1)
plt.scatter(x, data)

#  Insert code here  #


plt.show()