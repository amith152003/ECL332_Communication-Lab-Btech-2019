# Bit Error Rate (BER) Simulation and QPSK Constellation Analysis

This project demonstrates the simulation of Bit Error Rate (BER) for a Quadrature Phase Shift Keying (QPSK) modulation scheme under varying signal-to-noise ratio (SNR) conditions. It also provides a visualization of the QPSK constellation diagram.

---

## Table of Contents
1. [Overview](#overview)
2. [Code Features](#code-features)
3. [Steps Explained](#steps-explained)
4. [Visualization](#visualization)

---

## Overview
The project includes:
- **BER Simulation**: Calculates the BER for QPSK using both simulated and theoretical methods.
- **Constellation Visualization**: Displays the in-phase and quadrature components of QPSK symbols.

---

## Code Features
- **Random Symbol Generation**: Symbols are randomly generated for QPSK modulation (values 0, 1, 2, 3).
- **QPSK Mapping**: Maps symbols to constellation points.
- **Noise Addition**: Adds complex Gaussian noise to simulate a noisy communication channel.
- **BER Calculation**: Simulates BER by comparing transmitted and received symbols.
- **Theoretical BER**: Computes BER using the complementary error function.
- **Constellation Diagram**: Visualizes the QPSK signal in the complex plane.

---

## Steps Explained

### 1. Import Libraries
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc
```
    numpy: For numerical operations.
    matplotlib: For graph plotting.
    scipy.special: For theoretical BER calculation using erfc.

### 2. Define Parameters
```python
num_symbols = 1000000  # Number of symbols to simulate
EbNo_db_Range = np.arange(0, 11, 1)  # Eb/No range in dB
```
    Number of Symbols (num_symbols): Total QPSK symbols for simulation.
    Eb/No Range (EbNo_db_Range): SNR values in dB.

### 3. Generate Symbols and Map to QPSK
```python
symbols = np.random.randint(0, 4, num_symbols)  # Random QPSK symbols (0 to 3)
constellation = np.exp(1j * np.pi / 4 * np.array([1, 3, -3, -1]))  # Define QPSK constellation points
qpsk_symbols = constellation[symbols]  # Map symbols to QPSK constellation
```
    Maps QPSK symbols to their respective constellation points in the complex plane.

### 4. Simulate BER
```python
BER = []  # Initialize BER list
for EbNo in EbNo_db_Range:
    EbNo_lin = 10**(EbNo / 10)  # Convert Eb/No from dB to linear scale
    noise_power = 1 / (2 * EbNo_lin)  # Calculate noise power
    noise = np.sqrt(noise_power / 2) * (np.random.randn(num_symbols) + 1j * np.random.randn(num_symbols))  
    # Add complex Gaussian noise
    recieved_symbols = qpsk_symbols + noise  # Add noise to QPSK symbols
    estimated_symbols = np.argmin(abs(recieved_symbols[:, np.newaxis] - constellation), axis=1)  
    # Detect symbols
    num_error = np.sum(estimated_symbols != symbols)  # Count errors
    BER.append(num_error / (2 * num_symbols))  # Calculate BER
```
    Noise Simulation: Adds complex Gaussian noise.
    Symbol Detection: Finds the closest constellation point for each received symbol.
    Error Calculation: Compares transmitted and received symbols.

### 5. Theoretical BER
```python
BER_theory = 0.5 * erfc(np.sqrt(10**(EbNo_db_Range / 10)))
```
    Calculates theoretical BER for QPSK using erfc.

---

## Visualization
#### BER vs SNR
```python
plt.figure()
plt.semilogy(EbNo_db_Range, BER, '-', label='Simulated BER', linewidth=5)
plt.semilogy(EbNo_db_Range, BER_theory, '-o', label='Theoretical BER')
plt.xlabel("Eb/No dB (SNR)")
plt.ylabel("BER")
plt.legend()
plt.title("Error Probability of QPSK")
plt.grid()
```
    BER Plot: Compares simulated and theoretical BER on a semi-logarithmic scale.

#### QPSK Constellation Diagram
```python
plt.figure()
plt.plot(qpsk_symbols.real, qpsk_symbols.imag, 'o')
plt.xlabel("In-Phase")
plt.ylabel("Quadrature")
plt.title("Constellation Diagram of QPSK")
plt.grid()
```
    Displays the QPSK constellation points in the in-phase and quadrature plane.

#### Display Results
```python
plt.show()
```
    Displays the BER vs SNR plot and the QPSK constellation diagram.
