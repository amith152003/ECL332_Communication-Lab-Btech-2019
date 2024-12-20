# Pulse Shaping and Matched Filtering

This project demonstrates the process of digital signal transmission and reception using pulse shaping, addition of noise, and matched filtering. It includes generating a binary message, shaping the pulses using a raised cosine filter, simulating a noisy channel, and recovering the signal using a matched filter.

## Table of Contents
1. [Overview](#overview)
2. [Code Features](#code-features)
3. [Steps Explained](#steps-explained)
4. [Visualization](#visualization)

---

## Overview
This project implements:
- Binary message generation.
- Pulse shaping using a raised cosine filter.
- Noise addition to simulate a real-world channel.
- Signal recovery using a matched filter.

---

## Code Features
- **Message Generation**: Creates a binary sequence (0s and 1s).
- **Pulse Shaping**: Shapes the pulses using a raised cosine filter to minimize inter-symbol interference.
- **Noise Simulation**: Adds Additive White Gaussian Noise (AWGN) to simulate a noisy channel.
- **Matched Filtering**: Recovers the signal using correlation with a rectangular pulse.

---

## Steps Explained

### 1. Import Libraries
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import correlate
```
    numpy: For numerical operations and data manipulation.
    matplotlib: For visualizing signals and filters.
    scipy.signal: For performing correlation (matched filtering).

### 2. Message Generation
```python
N = 10  # Number of bits in the message
sps = 10  # Samples per symbol
data = np.random.randint(0, 2, N)  # Generate random binary data

x = np.array([])
for bit in data:
    pulse = np.zeros(sps)
    pulse[0] = 2 * bit - 1  # Assign +1 for bit 1 and -1 for bit 0
    x = np.concatenate((x, pulse))
```
    Binary Data: A random sequence of 0s and 1s.
    Samples per Symbol (sps): Determines the resolution of each pulse.
    Signal (x): Constructed by appending pulses for each bit.

### 3. Raised Cosine Filter
Define Filter Parameters
```python
num_taps = 101  # Number of filter coefficients
B = 0.4  # Roll-off factor
Ts = sps  # Symbol period

t = np.arange(num_taps) - (num_taps - 1) // 2
h = 1 / Ts * np.sinc(t / Ts) * np.cos(np.pi * B * t / Ts) / (1 - (2 * B * t / Ts) ** 2)
```
    Filter Parameters:
        Number of taps: Controls the length of the filter.
        Roll-off factor (B): Determines the bandwidth of the filter.
        Symbol period (Ts): Number of samples per symbol.
    Filter Coefficients (h): Calculated using the raised cosine formula.

Pulse Shaping
```python
x_shaped = np.convolve(x, h)
```
    Convolves the signal with the raised cosine filter to smoothen transitions between pulses.

### 4. Noise Addition
```python
awgn = np.random.normal(0, 1, 100)  # Generate Additive White Gaussian Noise
x_noise = x + awgn  # Add noise to the signal
```
    Adds noise to the signal to simulate transmission over a noisy channel.

### 5. Matched Filtering
```python
corr = correlate(x_noise, np.ones(100), mode="same") / 100
```
    Matched Filter Output (corr): Correlates the noisy signal with a rectangular pulse to recover the transmitted message.

---

## Visualization
Subplots

#### Original Transmitted Signal
```python
plt.figure()
plt.plot(x, '.-')
plt.title("Message")
```

#### Raised Cosine Filter
```python
plt.figure()
plt.plot(t, h, '.')
plt.title("Raised Cosine")
```

#### Pulse Shaped Signal
```python
plt.figure()
plt.plot(x_shaped)
plt.title("Pulse Shaping")
```

#### Noisy Signal
```python
plt.figure()
plt.plot(x_noise)
plt.title("Added Noise Signal")
```

#### Matched Filter Output
```python
    plt.figure()
    plt.plot(corr)
    plt.title("Matched Filter")
```

#### Show All Plots
```python
plt.show()
```
