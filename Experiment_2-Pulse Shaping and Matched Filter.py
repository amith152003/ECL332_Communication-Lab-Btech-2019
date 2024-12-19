import numpy as np    #To create arrays and other operation 
import matplotlib.pyplot as plt    #To plot the required arrays
from scipy.signal import correlate    #The correlation function

# Set parameters
N = 10          # Number of bits to transmit
sps = 10        # Samples per symbol (symbol rate)
data = np.random.randint(0, 2, N)  # Random binary data (0s and 1s)

# Initialize an empty array to store the shaped signal
x = np.array([])

# For each bit in the binary data, create a pulse and append it to the signal
for bit in data:
    pulse = np.zeros(sps)  # Create a zero pulse of length sps
    pulse[0] = 2 * bit - 1  # Set the first sample to 1 or -1 based on the bit
    x = np.concatenate((x, pulse))  # Append the pulse to the signal array

# Define the number of taps for the raised cosine filter
num_taps = 101
B = 0.4          # Roll-off factor for the raised cosine filter
Ts = sps         # Symbol period (samples per symbol)

# Create a time vector for the filter
t = np.arange(num_taps) - (num_taps - 1) // 2  # Centered time vector for filter

# Create the raised cosine filter using the given parameters
h = 1/Ts * np.sinc(t/Ts) * np.cos(np.pi * B * t/Ts) / (1 - (2*B*t/Ts)**2)

# Apply the pulse shaping filter (raised cosine filter) to the transmitted signal
x_shaped = np.convolve(x, h)

# Add noise to the signal by generating white Gaussian noise (AWGN)
awgn = np.random.normal(0, 1, 100)  # AWGN with mean=0 and variance=1
x_noise = x + awgn  # Add noise to the original signal

# Perform a matched filter (correlate with a filter of all ones)
corr = correlate(x_noise, np.ones(100), mode="same") / 100

# Plot the results

# Plot the original message (binary data signal)
plt.figure()
plt.plot(x, '.-')
plt.title("Message")

# Plot the raised cosine filter
plt.figure()
plt.plot(t, h, '.')
plt.title("Raised Cosine Filter")

# Plot the pulse-shaped signal after applying the raised cosine filter
plt.figure()
plt.plot(x_shaped)
plt.title("Pulse Shaping")

# Plot the signal after adding noise (AWGN)
plt.figure()
plt.plot(x_noise)
plt.title("Added Noise Signal")

# Plot the result of the matched filter operation (correlation result)
plt.figure()
plt.plot(corr)
plt.title("Matched Filter")

# Display all the plots
plt.show()
