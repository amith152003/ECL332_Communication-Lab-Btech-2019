import numpy as np    #This is used for calculations
import matplotlib.pyplot as plt    #This is to plot graphs

# Define parameters
amplitude = 1      # Amplitude of the sine wave
fm = 100           # Frequency of the sine wave in Hz
t = np.arange(0, 0.05, 0.0005)  # Time vector from 0 to 0.05 seconds with a step size of 0.0005s

#1. Generate a continuous sine wave signal 'x'
x = np.sin(2*np.pi*fm*t)  # Sine wave with frequency fm

#2. Create an offset sine wave 'x_offset' by adding 1 to 'x'
x_offset = x + 1  # Shift the sine wave upwards by 1 unit

#3. Create a sampled version of the sine wave 'x_s' based on a sampling frequency 'fs'
fs = 10*fm  # Sampling frequency is 10 times the frequency of the sine wave
Ts = 1/fs   # Sampling period (inverse of the sampling frequency)
n = np.random.randint(2, size = len(t))  # Generate random binary noise (not used in sampling directly)
nTs = n*Ts  # Multiplied noise by sampling period (though not used later)
T = np.arange(0, 0.05, Ts)  # New time vector for sampled signal
x_s = np.sin(2*np.pi*fm*T)  # Sampled sine wave signal

#4. Quantization: define levels for the quantization process
n = 3  # Number of bits for quantization
L = 2**n  # Calculate the number of quantization levels (2^n)
x_max = round(max(x))  # Maximum value of the sine wave
x_min = round(min(x))  # Minimum value of the sine wave
delta = (x_max - x_min)/2  # Half the difference between max and min values
Q_level = np.linspace(x_min, x_max, L+1)  # Quantization levels

# Generate a quantized signal using Q_levels
x_q = np.linspace(0, 2*x_max, L, endpoint = False)  # Quantization steps from 0 to 2 * x_max
t_1 = t[0:len(x_q)]  # Time vector for quantized signal

#5. Perform quantization by finding the nearest quantization level for each sample
x_q_1 = []  # Empty list to store the quantized values

for i in x_s:
    for j in Q_level:
        if i >= j:  # If the signal value is greater than or equal to the quantization level
            x_q_1.append(j)  # Append the quantization level
            break  # Break after the first match (quantization process)

# Calculate quantization error (difference between quantized signal and original)
e_q = x_q_1 - x_s  # Quantization error is the difference between quantized and original signal

# Create a list of values 'n' representing bit-depth for different gamma calculations
n = [5, 6, 7, 8, 9]
gamma = []  # List to store gamma values for each bit-depth

# Calculate gamma values based on bit-depth (empirical formula)
for i in range(len(n)):
    gamma.append(1.8 + 6*n[i])  # Gamma value calculation

# Plotting
plt.figure()

# Subplot 1: Plot the original sine wave
plt.subplot(2,2,1)
plt.plot(t, x)  # Plot the continuous sine wave
plt.grid()  # Show grid

# Subplot 2: Plot the offset sine wave
plt.subplot(2,2,2)
plt.plot(t, x_offset)  # Plot the sine wave with offset
plt.grid()  # Show grid

# Subplot 3: Plot the sampled sine wave using stem plot
plt.subplot(2,2,3)
plt.stem(T, x_s)  # Plot the sampled sine wave (discrete-time)
plt.grid()  # Show grid

# Subplot 4: Plot the quantized signal using step plot
plt.subplot(2,2,4)
plt.step(t_1, x_q)  # Plot the quantized sine wave (stepped representation)
plt.grid()  # Show grid

# Plot the gamma vs bit-depth graph
plt.figure()
plt.plot(n, gamma)  # Plot gamma vs. bit-depth (n)
plt.grid()  # Show grid

# Display the plots
plt.show()
