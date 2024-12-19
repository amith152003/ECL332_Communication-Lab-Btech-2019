import numpy as np  # Import numpy for numerical operations
import matplotlib.pyplot as plt  # Import matplotlib for plotting
from scipy.signal import correlate  # Import correlate function from scipy for signal processing

N = 10  # Number of bits in the message
sps = 10  # Samples per symbol
data = np.random.randint(0, 2, N)  # Generate a random binary data sequence (0s and 1s)

x = np.array([])  # Initialize an empty array to store the signal

for bit in data:  # Loop through each bit in the binary data sequence
    pulse = np.zeros(sps)  # Create an array of zeros with length equal to sps
    pulse[0] = 2 * bit - 1  # Assign +1 for bit 1 and -1 for bit 0
    x = np.concatenate((x, pulse))  # Append the pulse to the signal

num_taps = 101  # Number of filter coefficients for the raised cosine filter
B = 0.4  # Roll-off factor of the raised cosine filter
Ts = sps  # Symbol period (number of samples per symbol)

t = np.arange(num_taps) - (num_taps - 1) // 2  # Generate a symmetric time vector for the filter

# Create the raised cosine filter using its mathematical formula
h = 1 / Ts * np.sinc(t / Ts) * np.cos(np.pi * B * t / Ts) / (1 - (2 * B * t / Ts) ** 2)

x_shaped = np.convolve(x, h)  # Convolve the signal with the raised cosine filter to shape the pulses

awgn = np.random.normal(0, 1, 100)  # Generate Additive White Gaussian Noise (AWGN)
x_noise = x + awgn  # Add the noise to the transmitted signal to simulate a noisy channel

# Perform correlation of the noisy signal with a rectangular pulse to implement a matched filter
corr = correlate(x_noise, np.ones(100), mode="same") / 100  

plt.figure()  # Create a new figure
plt.plot(x, '.-')  # Plot the original transmitted signal
plt.title("Message")  # Title of the plot

plt.figure()  # Create a new figure
plt.plot(t, h, '.')  # Plot the raised cosine filter
plt.title("Raised Cosine")  # Title of the plot

plt.figure()  # Create a new figure
plt.plot(x_shaped)  # Plot the pulse-shaped signal
plt.title("Pulse Shaping")  # Title of the plot

plt.figure()  # Create a new figure
plt.plot(x_noise)  # Plot the noisy signal
plt.title("Added Noise Signal")  # Title of the plot

plt.figure()  # Create a new figure
plt.plot(corr)  # Plot the matched filter output
plt.title("Matched Filter")  # Title of the plot

plt.show()  # Display all the plots
