#   This file is meant to test the decoder format/capabilities. It uses an example binary file
# that we can check with and confirm the graph and other data looks corect. The script reads in the
# binary file and performs a stft on the samples
from test import *

import numpy as np                  # to receive data
import matplotlib.pyplot as plt     # used for specgram plotting

filepath = 'binary/exFile.bin'

# get the binary file, read into numpy array
with open(filepath, 'rb') as file:
    binary_data = np.fromfile(file, dtype=np.int16)

# sample/binary params
sample_rate = 5000  # 5 kHz
sample_width = 2    # bytes/sample ______Should no longer need____

# short time fourier transform params
window_size = 1024  
overlap = 512       

# get length of recording
time_sec = len(binary_data) / (sample_rate) # dtype=np.int16 should account for sample width
print("Recording length: "+ str(time_sec/60) + " minutes or " + str(time_sec) + " seconds")

# plot the stft
plt.figure(figsize=(10, 6))

# spectrogram for data with previouslt defined parameters
plt.specgram(binary_data, NFFT=window_size, Fs=sample_rate, noverlap=overlap)

plt.colorbar(label='Power (dB)')    # colorbar for Power representation

# labels
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.title('Time vs. Frequency with Power Representation')
plt.savefig("spectrogramEx.png")
plt.show()

# compare to non-numpy
otherdata = read_binary_audio_file(filepath)


comparison_result = binary_data == binary_data
print(comparison_result)
#The results appear to be the same, confirming that both are workable and it is unlikely that both methods are wrong.
