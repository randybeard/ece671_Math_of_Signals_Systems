import numpy as np
import scipy.io.wavfile as wav

# get the input and output files
[rateIn, inWav] = wav.read("mary_had_a_little_lamb_in.wav", 'r')
[rateOut, expectedOutWav] = wav.read("mary_had_a_little_lamb_out.wav", 'r')


# number of taps in the filter.
# The lower this number is, the worse the output sounds. If you do 300,
# it will have a lot less static, but will take much longer to run.
numberOfParameters = 5

n = expectedOutWav.size   # length of the expected output

h = np.zeros(numberOfParameters)  # desired impulse response
# convenience array used to shift through input (f)
fn = np.hstack((np.zeros(numberOfParameters - 1),
                inWav, np.zeros(numberOfParameters - 1)))

# set up the generated output
generated_output = np.zeros(n)

delta = .0001
# initialize P[0] without calculating inverse of R[0]
P = 1/delta * np.eye(numberOfParameters)

forgettingFactor = .98

# Loop over the input/output data and create the
for i in range(0, n):
    end_index = i + numberOfParameters
    q = fn[i:end_index]      # q update
    d = expectedOutWav[i]

    k = P @ q / (forgettingFactor + q.T @ P @ q)  # kalman gain vector
    filterOut = q @ h  # filter output
    generated_output[i] = filterOut

    e = d - generated_output[i]     # error

    h = h + k * e  # update of estimated parameters
    P = (P - np.outer(k, np.matmul(q, P))) / forgettingFactor    # P update

# write the output to a wav file
generated_output = generated_output.astype(np.int16)
wav.write("generated_out.wav", rateOut, generated_output)
