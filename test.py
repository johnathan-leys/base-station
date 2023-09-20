# Testing without using numpy
import matplotlib.pyplot as plt

def read_binary_audio_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            # Initialize an empty list to store the audio samples
            audio_samples = []

            # Read 2 bytes (1 sample) at a time
            while True:
                sample_bytes = file.read(2)  # 2 bytes per sample for int_16t in C
                if not sample_bytes:
                    break  

                # Convert the 2-byte binary data to a signed 16-bit integer
                sample_value = int.from_bytes(sample_bytes, byteorder='little', signed=True)

                # Append the sample to the list
                audio_samples.append(sample_value)

    except Exception as e:      # Catch any error
        print(f"An error occurred: {str(e)}")
        return None
    
    plt.figure(figsize=(10, 6))
    # spectrogram for data 
    plt.specgram(audio_samples, NFFT=1024, Fs=5000, noverlap=512)

    plt.colorbar(label='Power (dB)')    # Colorbar for Power representation

    # labels
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.title('Time vs. Frequency with Power Representation')
    plt.savefig("spectrogramEx2.png")
    plt.show()

    return audio_samples


if __name__ == '__main__':
    file_path = 'exFile.bin'
    binary_audio_data = read_binary_audio_file(file_path)
    print(f"Number of samples: {len(binary_audio_data)}")
 
