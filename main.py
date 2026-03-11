import matplotlib.pyplot as plt
from core.signal_generator import SignalGenerator
from utils.plotter import Plotter


# fs -> sampling frequency
sg = SignalGenerator(fs=44100)

# t, sine = sg.sine(frequency=1000, duration=0.01)
# Plotter.plot_time(t, sine, title="1kHz Sine Wave")

t, noise_sine = sg.noise_sine(1000, duration=0.01)
Plotter.plot_time(t, noise_sine, title="1kHz Sine Wave")

# t, sine = sg.sine(1000, duration=0.01)
# t, square = sg.square(1000, duration=0.01)

# Plotter.plot_multiple(
#     t,
#     [sine, square],
#     labels=["Sine", "Square"],
#     title="Sine vs Square"
# )
