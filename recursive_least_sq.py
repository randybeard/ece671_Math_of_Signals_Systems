import numpy as np
import scipy.io.wavfile as wav
import scipy.signal as signal


np.set_printoptions(precision=4)

# get the input and output files
[rateIn, inWav] = wav.read("mary_had_a_little_lamb_in.wav", 'r')
[rateOut, expectedOutWav] = wav.read("mary_had_a_little_lamb_out.wav", 'r')


# number of parameters:
numberOfParameters = 300

# this will hold the input data samples as they are pushed through the system
# frameOfInputData = np.zeros(numberOfParameters)

n = expectedOutWav.size   # iterations

h = np.zeros(numberOfParameters)  # desired impulse response
# convenience array used to shift through input (f)
fn = np.hstack((np.zeros(numberOfParameters - 1), inWav))
delta = .0001

# initialize P[0] without calculating inverse of R[0]
P = 1/delta * np.eye(numberOfParameters)

# set up the generated output
generated_output = np.zeros(expectedOutWav.size)

start = 0
while(expectedOutWav[start] == 0):
    start += 1

start = 0

forgettingFactor = .97
for i in range(start, n - numberOfParameters):

    end_index = i + numberOfParameters
    q = fn[i:end_index]      # q update
    d = expectedOutWav[i]

    k = P @ q / (forgettingFactor + q.T @ P @ q)  # kalman gain vector
    filterOut = q @ h  # filter output
    generated_output[i] = filterOut

    e = d - generated_output[i]     # error

    h = h + k * e  # update of estimated parameters
    # mid_step1 = np.matmul(q, P)
    # mid_step2 = np.outer(k, mid_step1)
    P = (P - np.outer(k, np.matmul(q, P))) / forgettingFactor    # P update

generated_output = generated_output.astype(np.int16)
wav.write("generated_out.wav", rateOut, generated_output)
