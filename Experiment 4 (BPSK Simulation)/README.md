# Bit Error Rate (BER) Simulation and BPSK Constellation Analysis

This project demonstrates the simulation of Bit Error Rate (BER) for a Binary Phase Shift Keying (BPSK) modulation scheme under different signal-to-noise ratio (SNR) conditions. It also visualizes the BPSK constellation diagram.

---

## Table of Contents
1. [Overview](#overview)
2. [Code Features](#code-features)
3. [Steps Explained](#steps-explained)
4. [Visualization](#visualization)

---

## Overview
The project covers:
- **BER Analysis**: Simulates and compares the theoretical and simulated BER for BPSK modulation.
- **Constellation Diagram**: Visualizes the in-phase and quadrature components of BPSK symbols.

---

## Code Features
- **Random Binary Data Generation**: Symbols are randomly generated as binary data (0s and 1s).
- **BPSK Mapping**: Maps binary symbols to BPSK symbols (`+1` and `-1`).
- **Gaussian Noise Addition**: Simulates channel noise based on SNR.
- **BER Calculation**: Simulates BER by comparing transmitted and received symbols.
- **Theoretical BER Comparison**: Computes theoretical BER using the complementary error function.
- **Constellation Visualization**: Displays the in-phase and quadrature components of the BPSK signal.

---

## Steps Explained

### 1. Import Libraries
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc
```
    numpy: For numerical computations.
    matplotlib: For plotting graphs.
    scipy.special: For the complementary error function used in theoretical BER calculations.

### 2. Define Parameters
```python
num_symbols = 1000000  # Number of symbols to simulate
EbNo_db_Range = np.arange(0, 11, 1)  # Range of Eb/No values in dB
```
    Number of Symbols (num_symbols): Total symbols for simulation.
    Eb/No Range (EbNo_db_Range): Signal-to-noise ratio values in dB.

### 3. Generate Random Data and Map to BPSK
```python
symbols = np.random.randint(0, 2, num_symbols)  # Random binary data
bpsk_symbols = 2 * symbols - 1  # Map binary data to BPSK (+1 for 1, -1 for 0)
```
    Maps binary data to BPSK modulation.

### 4. Add Noise and Simulate BER
```python
BER = []  # Initialize BER list
for EbNo in EbNo_db_Range:
    EbNo_lin = 10**(EbNo / 10)  # Convert Eb/No from dB to linear scale
    noise_power = 1 / (2 * EbNo_lin)  # Noise power
    noise = np.sqrt(noise_power) * np.random.randn(num_symbols)  # Generate noise
    recieved_symbols = bpsk_symbols + noise  # Add noise to BPSK symbols
    estimated_symbols = (recieved_symbols > 0).astype(int)  # Detect symbols
    num_error = sum(estimated_symbols != symbols)  # Count errors
    BER.append(num_error / num_symbols)  # Store BER
```
    Noise Addition: Simulates channel noise for varying SNR levels.
    Symbol Detection: Threshold-based detection of received symbols.
    Error Calculation: Compares received symbols with original symbols to calculate BER.

### 5. Theoretical BER Calculation
```python
BER_theory = 0.5 * erfc(np.sqrt(10**(EbNo_db_Range / 10)))
```
    Uses the complementary error function for theoretical BER computation.

---

## Visualization
#### BER vs SNR
```python
plt.figure()
plt.semilogy(EbNo_db_Range, BER, '-', label='Simulated BER', linewidth=5)
plt.semilogy(EbNo_db_Range, BER_theory, '-o', label='Theoretical BER')
plt.xlabel("Eb/No (dB)")
plt.ylabel("BER (Bit Error Rate)")
plt.legend()
plt.grid()
plt.title("BER vs SNR")
```
    BER Plot: Compares simulated and theoretical BER on a semi-logarithmic scale.

#### BPSK Constellation Diagram
```python
plt.figure()
plt.plot(bpsk_symbols.real, bpsk_symbols.imag, 'o')
plt.xlabel("Inphase")
plt.ylabel("Quadrature")
plt.grid()
plt.title("Constellation Diagram of BPSK")
```
    Displays the BPSK symbols on the in-phase and quadrature axes.

#### Display Plots
```python
plt.show()
```
    Displays the generated BER plot and constellation diagram.
