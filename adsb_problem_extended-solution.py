# SOLUTION #
import numpy as np
import matplotlib.pyplot as plt

num_samples = 10000
order_of_polynomial = 10

# Download CSV file from the link provided
data = np.genfromtxt("adsb_data.csv", delimiter=",")
x = np.linspace(0, 5, num_samples)

# Plot data
plt.figure(1)
plt.scatter(x, data, s=2)


#  Insert code here  #

# Create A and y
A = np.zeros((num_samples, order_of_polynomial + 1))
y = np.zeros(num_samples)

# Populate A and y
for i in range(num_samples):
    for j in range(order_of_polynomial + 1):
        A[i][j] = (i / num_samples)**(order_of_polynomial - j)
    y[i] = data[i]

# Solve for coefficients
h = np.linalg.inv(A.transpose() @ A) @ A.transpose() @ y

# Filter data
filtered_data = A @ h

# Plot filtered data
plt.figure(2)
plt.scatter(x, filtered_data, s=2)

# Estimate successful decode probability at 10 UAS/km^2
estimated_value = 0
for i in range(order_of_polynomial + 1):
    estimated_value += h[i]*10**(order_of_polynomial - i)
print("Estimated successful decode probability at 10 UAS/km^2:", estimated_value)

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

# Plot weighted filtered data
plt.figure(3)
plt.scatter(x, weighted_filtered_data, s=2)

# Estimate successful decode probability at 10 UAS/km^2
estimated_value_weighted = 0
for i in range(order_of_polynomial + 1):
    estimated_value_weighted += h_weighted[i]*10**(order_of_polynomial - i)
print("Estimated successful decode probability at 10 UAS/km^2, weighted:", estimated_value_weighted)

plt.show()

#  EXPLANATIONS  #
# With the polynomial order set to 10, the curves do seem to fit the data much better,
# especially for UAS densities below 2 UAS/km^2. This is because we are adding
# polynomials with different coefficients until they manage to fit all the curves of
# the data. The estimations for decode probabilities are way off now, and this is because
# the coefficients are only trying to fit the curve to the data that we have instead of
# trying to fit the curve to what the data probably would be at higher values of UAS density.
# With the polynomial order set to 100, the curve doesn't seem to match the data at all anymore.
