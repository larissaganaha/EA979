from numpy.fft import *
from numpy import log10, sqrt, array, zeros, ones, multiply
import math
import wave
import struct
import matplotlib.pyplot as plt


def get_samples(file):

    waveFile = wave.open(file, 'r')
    samples = []

    # Gets total number of frames
    length = waveFile.getnframes()

    # Read them into the frames array
    for i in range(0,length):
        waveData = waveFile.readframes(1)
        data = struct.unpack("%ih"%2, waveData)

        # After unpacking, each data array here is actually an array of ints
        # The length of the array depends on the number of channels you have

        # Drop to mono channel
        samples.append(int(data[0]))

    samples = array(samples)
    return samples



# Example manipulations
samples = get_samples('maybe-next-time.wav')
plt.plot(samples)
plt.show()
# # Compute the FFT of the samples (gets the frequencies used)
# freq_domain = fft(samples)
# plt.plot(freq_domain)
# plt.show()
#
# # Compute energy of samples by squaring and summing
# def energy(samples):
#     return sum([x**2 for x in samples])
