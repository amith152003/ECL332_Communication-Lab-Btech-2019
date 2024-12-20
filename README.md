# Communication Lab (ECL332) - B.Tech Scheme 2019

This repository provides Python code implementations and simulations for the **Communication Lab (ECL332)** course, part of the B.Tech Scheme 2019 curriculum. These codes aim to help students understand various communication techniques and concepts used in modern communication systems. The code snippets and simulations provided here assist in visualizing modulation schemes, error performance, and signal processing techniques used in communication systems.

---

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Modules](#modules)
  - [Analog to Digital Conversion](#analog-to-digital-conversion)
  - [Baseband Modulation and Pulse Shaping](#baseband-modulation-and-pulse-shaping)
  - [Eye Diagram Analysis](#eye-diagram-analysis)
  - [BPSK Simulation](#bpsk-simulation)
  - [QPSK Simulation](#qpsk-simulation)
- [License](#license)

---

## Overview

This repository is designed for students to explore different communication techniques and understand their implementations through Python. The repository includes simulations and code demonstrations for various concepts such as:

- **Analog to Digital Conversion**: Understanding sine wave generation, offset addition, sampling, quantization, and calculating Signal-to-Noise Ratio (SNR).
- **Baseband Modulation**: Pulse shaping, filtering, and matched filter response.
- **Modulation Techniques**: BPSK and QPSK modulation and demodulation.
- **Error Rate Analysis**: Bit Error Rate (BER) vs Signal-to-Noise Ratio (SNR) for BPSK and QPSK.
- **Constellation Diagrams**: Visualization of modulation schemes.
- **Eye Diagrams**: Analyzing the effect of inter-symbol interference (ISI) and noise.

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

### Analog to Digital Conversion

This module focuses on understanding the conversion process from analog signals to digital signals. The following topics are covered:

- **Sine Wave Generation**: Generating sine waves with specific frequency and amplitude.
- **Offset Addition**: Introducing DC offsets to sine waves.
- **Sampling**: Sampling the sine wave at discrete time intervals.
- **Quantization**: Quantizing the sampled signal to a finite number of levels.
- **Signal-to-Noise Ratio (SNR)**: Calculating SNR to analyze the performance of the quantization process.

Visualization includes the original sine wave, sampled signals, quantized signals, and SNR plots.

---

### Baseband Modulation and Pulse Shaping

This module demonstrates baseband modulation with pulse shaping and filtering. Key features include:

- **Raised Cosine Filters**: Pulse shaping using raised cosine filters to minimize ISI.
- **Matched Filter Response**: Visualization of the matched filter's effect on the received signal.

Outputs include:
- Transmitted and received signals.
- Shaped pulses and their spectra.

---

### Eye Diagram Analysis

This module demonstrates how to generate and analyze eye diagrams to study the effects of ISI and noise in communication systems.

Key features include:
- **Signal Visualization**: Overlay of multiple signal traces to form an eye diagram.
- **ISI Detection**: Observing the degree of signal overlap and distortion.
- **Noise Effects**: Analyzing the impact of AWGN on the eye diagram.

---

### BPSK Simulation

This section simulates Binary Phase Shift Keying (BPSK) communication in an Additive White Gaussian Noise (AWGN) channel. Features include:

- **BER Analysis**: Computing the Bit Error Rate (BER) and comparing it with theoretical BER values for varying Eb/No ratios.
- **Signal Visualization**: Constellation diagrams for BPSK symbols.
- **Performance Metrics**: SNR vs BER plots.

Outputs include theoretical and simulated BER vs SNR graphs and BPSK constellation diagrams.

---

### QPSK Simulation

This module explores Quadrature Phase Shift Keying (QPSK) modulation. Key features include:

- **Modulation and Demodulation**: Implementing QPSK transmission and reception in AWGN.
- **BER Analysis**: Simulating and comparing BER with theoretical values for varying Eb/No.
- **Constellation Diagram**: Visualizing QPSK symbol placement in the I-Q plane.

Outputs include QPSK constellation diagrams and BER vs SNR graphs.

---

## License

This repository is open-source and available under the Apache 2.0 License. You are free to use, modify, and distribute the code for both academic and commercial purposes, provided proper attribution is given. See the LICENSE file for detailed terms and conditions.

---

Explore, learn, and visualize communication systems with this Communication Lab repository. Contributions and feedback are welcome to enhance the learning experience for students!
