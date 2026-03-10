import matplotlib.pyplot as plt
from core.signal_generator import SignalGenerator

sampling_frequency = 44100 

generate = SignalGenerator(sampling_frequency)

# t, sine_signal = generate.sine(
#     frequency = 1000,
#     duration = 0.01
# )

t, cosine_signal = generate.cosine(
    frequency = 500,
    duration = 0.05
)

# plt.plot(t, sine_signal)
plt.plot(t, cosine_signal)

plt.show()

