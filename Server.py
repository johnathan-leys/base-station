import numpy as np

from bokeh.plotting import figure, show, output_file
from bokeh.models import ColorBar, LinearColorMapper, BasicTicker

from scipy.signal import stft


def binary_to_numpy(filename):
    # Read binary file
    with open(filename, 'rb') as f:
        data = f.read()
    
    # Convert to numpy array
    audio_data = np.frombuffer(data, dtype=np.int16)
    
    # Normalize to float in range [-1, 1]
    audio_data = audio_data.astype(np.float32) / np.iinfo(np.int16).max
    return audio_data


def compute_spectrogram_array(audio_data, sample_rate):
    # Compute the short-time Fourier transform using scipy
    f, t, Zxx = stft(audio_data, fs=sample_rate, nperseg=1024) # Modify nperseg, but 1024 should work
    D = np.abs(Zxx)

    # Convert an amplitude spectrogram to dB-scaled spectrogram
    spectrogram = amplitude_to_db(D)
    return spectrogram

def amplitude_to_db(spectrogram):
    # Avoid log of zero by adding a small number
    spectrogram = 20 * np.log10(np.maximum(spectrogram, 1e-7))
    return spectrogram

def display_interactive_spectrogram(spectrogram, sample_rate):
    # Set up time and frequency axes
    time = np.linspace(0, len(spectrogram[0]) * 512 / sample_rate, len(spectrogram[0]))
    freq = np.linspace(0, sample_rate/2, len(spectrogram))

    # Create a Bokeh figure
    p = figure(x_range=(time[0], time[-1]), y_range=(freq[0], freq[-1]),
               x_axis_label="Time (s)", y_axis_label="Frequency (Hz)", tools="pan,box_zoom,wheel_zoom,reset")

    # Create a color mapper
    color_mapper = LinearColorMapper(palette="Viridis256", low=spectrogram.min(), high=spectrogram.max())
    
    # Display image
    p.image(image=[spectrogram], x=time[0], y=freq[0], dw=time[-1], dh=freq[-1], color_mapper=color_mapper)

    # Set up color bar
    color_bar = ColorBar(color_mapper=color_mapper, ticker=BasicTicker(), label_standoff=12)
    p.add_layout(color_bar, 'right')
    
    # Show plot
    output_file("interactive_spectrogram.html")
    show(p, notebook_handle=True)

audio_data = binary_to_numpy('Combined/combined.bin')
spectrogram = compute_spectrogram_array(audio_data, 5000)  # 5 kHz sample rate
display_interactive_spectrogram(spectrogram, 5000)
