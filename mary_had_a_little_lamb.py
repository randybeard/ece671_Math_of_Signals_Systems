import numpy as np
import scipy.io.wavfile as wav

# get the input and output files
[rateIn, inWav] = wav.read("mary_had_a_little_lamb_in.wav", 'r')
[rateOut, expectedOutWav] = wav.read("mary_had_a_little_lamb_out.wav", 'r')

# number of taps in the filter.
numberOfParameters = 5

n = expectedOutWav.size   # length of the expected output

# convenience array used to shift through input. The beginning is padded with zeros,
# and the end is also padded with zeros.
fn = np.hstack((np.zeros(numberOfParameters - 1),
                inWav, np.zeros(numberOfParameters - 1)))

# impulse response of system we are generating
h = np.zeros(numberOfParameters)

# preallocate the output that we will be generating
generated_output = np.zeros(n)

'''
WRITE YOUR CODE HERE.

- fn is an array of inputs that has already been zero padded
- h is the array for the system coefficients that your code will be using to 
  approximate the system
- generated_output is an array that you should write each output of your system to.
  This will be saved to a .wav file that you can listen to once the system is done
  processing.

You will need to:
1. set up P
2. loop through the inputs and outputs to compute P, k, h, and the generated_output
   at each time step. Save your guessed outputs to the generated_output array for
   it to be written to a wave file at the end of the processing
'''

# write the output to a wav file.
generated_output = generated_output.astype(np.int16)
wav.write("generated_out.wav", rateOut, generated_output)
