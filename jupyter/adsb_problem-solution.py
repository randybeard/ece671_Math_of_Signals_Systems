# SOLUTION #
import numpy as np
import matplotlib.pyplot as plt

num_samples = 10000

# Download CSV file from the link provided
data = np.genfromtxt("adsb_data.csv", delimiter=",")
x = np.linspace(0, 5, num_samples)

# Plot data
plt.figure(1)
plt.scatter(x, data, s=2)


#  Insert code here  #

# Create A and y
A = np.zeros((num_samples, 2))
y = np.zeros(num_samples)

# Populate A and y
for i in range(num_samples):
    A[i][0] = i / num_samples
    A[i][1] = 1.0
    y[i] = data[i]

# Solve for coefficients
h = np.linalg.inv(A.transpose() @ A) @ A.transpose() @ y

# Filter data
filtered_data = A @ h

# Plot filtered data, estimate successful decode probability at 10 UAS/km^2
plt.figure(2)
plt.scatter(x, filtered_data, s=2)
print("Estimated successful decode probability at 10 UAS/km^2:", h[0]*(10) + h[1])

# Create and populate weighing matrix
# Weigh the first 2000 samples much less
W = np.zeros((num_samples, num_samples))
for i in range(num_samples):
    if i < 2000:
        W[i][i] = 1
    else:
        W[i][i] = 100

# Solve for weighted coefficients
h_weighted = np.linalg.inv(A.transpose() @ W @ A) @ A.transpose() @ W @ y

# Filter using weighted coefficients
weighted_filtered_data = A @ h

# Plot weighted filtered data, estimate successful decode probability at 10 UAS/km^2
plt.figure(3)
plt.scatter(x, weighted_filtered_data, s=2)
print("Estimated successful decode probability at 10 UAS/km^2, weighted:", h_weighted[0]*(10) + h_weighted[1])

plt.show()