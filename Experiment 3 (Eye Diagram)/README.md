# Eye Diagram Using Raised Cosine Filter

This project demonstrates the simulation of a baseband signal and its corresponding eye diagram using a raised cosine filter for pulse shaping. The process involves generating a random binary sequence, applying pulse shaping with the raised cosine filter, and visualizing the results.

---

## Table of Contents
1. [Overview](#overview)
2. [Code Features](#code-features)
3. [Steps Explained](#steps-explained)
4. [Visualization](#visualization)

---

## Overview
This project showcases:
- Pulse shaping using a raised cosine filter to minimize inter-symbol interference.
- Generation of a baseband signal.
- Visualization of the eye diagram to analyze signal quality.

---

## Code Features
- **Random Binary Sequence Generation**: Symbols are randomly chosen as either `-1` or `+1`.
- **Raised Cosine Filter Design**: Implements a raised cosine filter with a given roll-off factor and span.
- **Upsampling and Filtering**: Uses `upfirdn` to upsample and filter the signal for smooth transitions.
- **Eye Diagram Visualization**: Displays overlapping signal segments to evaluate signal quality.

---

## Steps Explained

### 1. Import Libraries
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import upfirdn
```
    numpy: For numerical calculations and data manipulation.
    matplotlib: For plotting the baseband signal and eye diagram.
    scipy.signal: For upsampling and filtering using the upfirdn function.

### 2. Define Parameters
```python
N = 100       # Number of symbols in the data sequence
span = 10     # Filter span in symbol periods
sps = 8       # Samples per symbol
rolloff = 0.4 # Roll-off factor for the raised cosine filter
```
    Number of Symbols (N): Total symbols in the sequence.
    Filter Span: Determines the duration of the filter response.
    Samples per Symbol (sps): Defines the sampling rate.
    Roll-off Factor (rolloff): Determines the excess bandwidth of the filter.

### 3. Raised Cosine Filter Design
Function Definition
```python
def rsed_cos(rolloff, span, sps):
    t = np.linspace(-span/2, span/2, sps*span)  # Time vector
    response = np.zeros(sps*span)
    for i in range(sps*span):
        if abs(t[i]) == (span/(2*rolloff)):
            response[i] = np.sinc(span/(2*rolloff)) * np.pi / 4
        else:
            response[i] = (
                np.sinc(t[i]) 
                * np.cos(np.pi * rolloff * t[i] / span) 
                / (1 - (2 * rolloff * t[i] / span)**2)
            )
    return response
```
    Special Case Handling: Avoids singularity for specific time points.
    Filter Response (response): Computed for each time point.

### 4. Filter Generation
```python
rct_filt = rsed_cos(rolloff, span, sps)
```
    Filter Application: Generates the raised cosine filter based on defined parameters.

### 5. Data Generation and Pulse Shaping
Binary Sequence
```python
data = np.random.choice([-1, 1], size=N)  # Random sequence of -1 and +1
```
    Generates a random binary sequence representing the symbols.

### 6. Upsampling and Filtering
```python
UP_s = upfirdn(rct_filt, data, up=10)
```
    Upsampling: Increases the resolution of the signal.
    Filtering: Applies the raised cosine filter to smooth transitions.

---

## Visualization
#### Baseband Signal
```python
plt.figure()
plt.plot(UP_s)
plt.title("Baseband Signal")
plt.grid()
```
    Displays the upsampled and filtered baseband signal.

#### Eye Diagram
```python
plt.figure()
for i in range(N):
    plt.plot(UP_s[i*10:(i+2)*10], linewidth=0.6)
plt.title("Eye Diagram")
plt.grid()
```
    Eye Diagram: Overlays signal segments to analyze symbol transitions.

#### Show Plots
```python
plt.show()
```
    Displays the generated plots.
