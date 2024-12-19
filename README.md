# Communication Lab (ECL332) - B.Tech Scheme 2019

This repository provides Python code implementations and simulations for the **Communication Lab (ECL332)** course, part of the B.Tech Scheme 2019 curriculum. These codes aim to help students understand various communication techniques and concepts used in modern communication systems. The code snippets and simulations provided here assist in visualizing modulation schemes, error performance, and signal processing techniques used in communication systems.

---

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Modules](#modules)
  - [Baseband Modulation and Pulse Shaping](#baseband-modulation-and-pulse-shaping)
  - [BPSK Simulation](#bpsk-simulation)
  - [QPSK Simulation](#qpsk-simulation)
  - [Raised Cosine Filtering](#raised-cosine-filtering)
  - [BER vs SNR](#ber-vs-snr)
- [License](#license)

---

## Overview

This repository is designed for students to explore different communication techniques and understand their implementations through Python. The repository includes simulations related to:

- **Baseband Modulation**: Pulse shaping, filtering, and noise analysis.
- **Modulation Techniques**: BPSK and QPSK modulation and demodulation.
- **Error Rate Analysis**: Bit Error Rate (BER) vs Signal-to-Noise Ratio (SNR) for BPSK and QPSK.
- **Constellation Diagrams**: Visualization of modulation schemes.

---

## Prerequisites

Before running the code, ensure you have the following Python libraries installed:

- `numpy`
- `matplotlib`
- `scipy`

You can install these dependencies by running:

```bash
pip install numpy matplotlib scipy
```

---

## Modules
### Baseband Modulation and Pulse Shaping
This module demonstrates baseband modulation with pulse shaping. It includes a simple implementation of BPSK modulation, pulse shaping using raised cosine filters, and visualizations of the transmitted signal, pulse shaping, and matched filter response.

### BPSK Simulation
This part of the project simulates Binary Phase Shift Keying (BPSK) communication in an Additive White Gaussian Noise (AWGN) channel. The simulation computes the Bit Error Rate (BER) and compares it with the theoretical BER for varying values of Eb/No.

### QPSK Simulation
This section focuses on Quadrature Phase Shift Keying (QPSK) modulation and its performance analysis in an AWGN channel. The simulated BER is compared with the theoretical BER for different Eb/No values. The QPSK constellation diagram is also visualized.

### Raised Cosine Filtering
This part explores the effect of raised cosine filtering for pulse shaping in communication systems. The code simulates the transmission of baseband signals, incorporating pulse shaping and upsampling.

### BER vs SNR
This module calculates and plots the Bit Error Rate (BER) versus Signal-to-Noise Ratio (SNR) for different modulation schemes. The simulated results are compared with theoretical calculations.

---

## License
This repository is open-source and available under the Apache 2.0 License. You are free to use, modify, and distribute the code for both academic and commercial purposes, with the condition that proper attribution is provided. See the LICENSE file for more details.
