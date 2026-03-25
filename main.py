import matplotlib.pyplot as plt
from core.signal_generator import SignalGenerator
from utils.plotter import Plotter
import numpy as np

# fs -> sampling frequency
sg = SignalGenerator(fs=44100)

t, sine_1k = sg.sine(frequency=1234, duration=0.01)
t, sine_3k = sg.sine(frequency=3000, amplitude=0.5, duration=0.01)
# t, noise = sg.noise(duration=0.01)

mixed_sine_signal = sine_1k + sine_3k 
# mixed_sine_signal = sine_1k + sine_3k + noise 
Plotter.plot_time(t, mixed_sine_signal)


# sampling and nyquist
sampling_freq = 44100
sampling_time = 1 / sampling_freq
nyquist_freq = sampling_freq / 2


n_samples = mixed_sine_signal.size
half_n = n_samples // 2
fft_result = np.fft.fft(mixed_sine_signal)


fft_magnitude = np.abs(fft_result)
fft_magnitude = fft_magnitude[0:half_n]
normalized_magnitude = fft_magnitude / ( n_samples / 2)

freq_axis = np.fft.fftfreq(n_samples, d=sampling_time)
freq_axis = freq_axis[0:half_n]

sorted_indices = np.argsort(normalized_magnitude)
top_indices = sorted_indices[-2:][::-1]     # last two values and revers them

for i, idx in enumerate(top_indices):
    print(f"Peak {i+1}: Frequency = {freq_axis[idx]}, Amplitude = {normalized_magnitude[idx]}")

plt.plot(freq_axis, normalized_magnitude)
plt.show()
