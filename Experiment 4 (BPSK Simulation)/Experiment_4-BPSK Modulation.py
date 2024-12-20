import numpy as np  # Import numpy for numerical operations
import matplotlib.pyplot as plt  # Import matplotlib for plotting
from scipy.special import erfc  # Import complementary error function for theoretical BER calculation

num_symbols = 1000000  # Number of symbols to simulate

EbNo_db_Range = np.arange(0, 11, 1)  # Range of Eb/No values in dB from 0 to 10
symbols = np.random.randint(0, 2, num_symbols)  # Generate random binary data (0s and 1s)
bpsk_symbols = 2 * symbols - 1  # Map binary data to BPSK symbols (+1 for 1, -1 for 0)
BER = []  # Initialize an empty list to store the simulated BER values

for EbNo in EbNo_db_Range:  # Loop through each Eb/No value
    EbNo_lin = 10**(EbNo / 10)  # Convert Eb/No from dB to linear scale
    noise_power = 1 / (2 * EbNo_lin)  # Calculate noise power based on Eb/No
    noise = np.sqrt(noise_power) * np.random.randn(num_symbols)  # Generate Gaussian noise

    recieved_symbols = bpsk_symbols + noise  # Add noise to the transmitted BPSK symbols
    estimated_symbols = (recieved_symbols > 0).astype(int)  # Detect received symbols (threshold at 0)

    num_error = sum(estimated_symbols != symbols)  # Count the number of errors
    BER.append(num_error / num_symbols)  # Calculate and store BER for this Eb/No

BER_theory = 0.5 * erfc(np.sqrt(10**(EbNo_db_Range / 10)))  # Calculate theoretical BER using complementary error function

plt.figure()  # Create a new figure
plt.semilogy(EbNo_db_Range, BER, '-', label='Simulated BER', linewidth=5)  # Plot simulated BER (log scale)
plt.semilogy(EbNo_db_Range, BER_theory, '-o', label='Theoretical BER')  # Plot theoretical BER
plt.xlabel("Eb/No (dB)")  # Label x-axis as Eb/No in dB
plt.ylabel("BER (Bit Error Rate)")  # Label y-axis as BER
plt.legend()  # Add legend to distinguish between simulated and theoretical curves
plt.grid()  # Enable grid for better visualization
plt.title("BER vs SNR")  # Title of the plot

plt.figure()  # Create a new figure
plt.plot(bpsk_symbols.real, bpsk_symbols.imag, 'o')  # Plot BPSK constellation (in-phase and quadrature components)
plt.xlabel("Inphase")  # Label x-axis as in-phase component
plt.ylabel("Quadrature")  # Label y-axis as quadrature component
plt.grid()  # Enable grid for better visualization
plt.title("Constellation Diagram of BPSK")  # Title of the constellation diagram

plt.show()  # Display all the plots

