#   This file is meant to test the decoder format/capabilities. It uses an example binary file
# that we can check with and confirm the graph and other data looks corect. The script reads in the
# binary file and performs a stft on the samples

import numpy as np                  # to receive data
import matplotlib.pyplot as plt     # used for specgram plotting

# get the binary file, read into numpy array
with open('exFile.bin', 'rb') as file:
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
plt.figure(figsize=(15, 9))

# spectrogram for data with previouslt defined parameters
plt.specgram(binary_data, NFFT=window_size, Fs=sample_rate, noverlap=overlap, cmap='viridis')

plt.colorbar(label='Power (dB)')    # colorbar for Power representation

# labels
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.title('Time vs. Frequency with Power Representation')

plt.show()
