# RF Lab

A small Python project for experimenting with **signal generation and DSP fundamentals**.

The goal of this project is to build a personal RF/DSP playground where different signal processing concepts can be explored and visualized using Python.

Currently the project supports basic **signal generation and visualization**.

---

# Current Features

### Signal Generator

The project currently includes a simple signal generator that can generate:

* Sine waves
* Cosine waves

The signals are generated using a configurable **sampling frequency** and **time duration**.

---

# Project Structure

```
rflab/
│
├── main.py
│
├── core/
│   ├── __init__.py
│   └── signal_generator.py
│
└── README.md
```

---

# Requirements

The project currently uses:

* Python
* NumPy
* Matplotlib

If using Conda, these packages can be installed inside your environment.

---

# Example Usage

Example from `main.py`:

```python
import matplotlib.pyplot as plt
from core.signal_generator import SignalGenerator

sampling_frequency = 44100

generate = SignalGenerator(sampling_frequency)

t, cosine_signal = generate.cosine(
    frequency=500,
    duration=0.05
)

plt.plot(t, cosine_signal)
plt.show()
```

This will generate and plot a cosine signal.

---

# What This Project Is For

This project is mainly for learning and experimenting with concepts such as:

* Sampling frequency
* Sampling period
* Signal generation
* Time domain signals
* DSP fundamentals

More features will be added gradually as the project evolves.

---

# Author

Mohammed Gayazuddin

