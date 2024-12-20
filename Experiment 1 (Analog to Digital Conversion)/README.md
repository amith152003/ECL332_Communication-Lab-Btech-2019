# Analog to Digital Signal Conversion

This project demonstrates various signal processing steps, including generating a sine wave, sampling it, quantizing it, and analyzing quantization errors and gamma values. 

## Table of Contents
1. [Overview](#overview)
2. [Code Features](#code-features)
3. [Steps Explained](#steps-explained)
4. [Visualization](#visualization)


---

## Overview
This project uses Python libraries like `numpy` and `matplotlib` to:
- Generate and manipulate sine waves.
- Perform sampling and quantization.
- Visualize the results in a step-by-step manner.

---

## Code Features
- **Generate Sine Wave**: Creates a continuous sine wave signal and an offset version.
- **Sampling**: Converts the continuous signal into a discrete sampled version.
- **Quantization**: Approximates signal values to predefined levels based on bit depth.
- **Error Calculation**: Computes the difference between the quantized and original sampled signals.
- **Gamma Analysis**: Empirically evaluates gamma values for different bit depths.

---

## Steps Explained

### 1. Import Libraries
```python
import numpy as np
import matplotlib.pyplot as plt
```
    numpy: For numerical calculations and signal generation.
    matplotlib: For plotting graphs.

### 2. Define Parameters
```python
amplitude = 1
fm = 100
t = np.arange(0, 0.05, 0.0005)
```
    Amplitude: Peak value of the sine wave.
    Frequency (fm): Cycles per second (in Hz).
    Time vector (t): Defines the signal's time range and resolution.

### 3. Generate the Sine Wave
```python
x = np.sin(2*np.pi*fm*t)
x_offset = x + 1
```
    x: Original sine wave.
    x_offset: Sine wave shifted upwards by 1 unit.

### 4. Sample the Sine Wave
```python
fs = 10*fm
Ts = 1/fs
T = np.arange(0, 0.05, Ts)
x_s = np.sin(2*np.pi*fm*T)
```
    Sampling Frequency (fs): Frequency at which the signal is sampled.
    Sampled Signal (x_s): Discrete representation of the sine wave.

### 5. Quantization
Define Quantization Levels
```python
n = 3
L = 2**n
x_max = round(max(x))
x_min = round(min(x))
delta = (x_max - x_min)/2
Q_level = np.linspace(x_min, x_max, L+1)
```
    Quantization Levels (L): Determined by the number of bits (n).
    Quantization Steps (delta): Step size between levels.

Quantize the Signal
```python
x_q_1 = []
for i in x_s:
    for j in Q_level:
        if i >= j:
            x_q_1.append(j)
            break
```
    Assigns each sampled value to the nearest quantization level.

### 6. Calculate Quantization Error
```python
e_q = x_q_1 - x_s
```
    Quantization Error (e_q): Difference between the quantized and original signal.

### 7. Gamma Calculation
```python
n = [5, 6, 7, 8, 9]
gamma = []
for i in range(len(n)):
    gamma.append(1.8 + 6*n[i])
```
Calculates gamma values empirically based on bit-depth.

## Visualization
Subplots

#### Original Sine Wave
```python
plt.subplot(2,2,1)
plt.plot(t, x)
```

#### Offset Sine Wave
```python
plt.subplot(2,2,2)
plt.plot(t, x_offset)
```

#### Sampled Sine Wave
```python
plt.subplot(2,2,3)
plt.stem(T, x_s)
```

#### Quantized Signal
```python
plt.subplot(2,2,4)
plt.step(t_1, x_q)
```

#### Gamma vs Bit-Depth Plot
```python
plt.figure()
plt.plot(n, gamma)
```

#### Show Plots
```python
plt.show()
```
