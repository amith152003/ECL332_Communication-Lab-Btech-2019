import numpy as np  # Import numpy for numerical operations
import matplotlib.pyplot as plt  # Import matplotlib for plotting
from scipy.special import erfc  # Import complementary error function for theoretical BER calculation

num_symbols = 1000000  # Number of symbols to simulate
EbNo_db_Range = np.arange(0, 11, 1)  # Range of Eb/No values in dB (from 0 to 10)

symbols = np.random.randint(0, 4, num_symbols)  # Generate random symbols (0, 1, 2, 3 for QPSK)
constellation = np.exp(1j * np.pi / 4 * np.array([1, 3, -3, -1]))  # Define QPSK constellation points
qpsk_symbols = constellation[symbols]  # Map symbols to QPSK constellation points

BER = []  # Initialize an empty list to store the simulated BER values

for EbNo in EbNo_db_Range:  # Loop through each Eb/No value
    EbNo_lin = 10**(EbNo / 10)  # Convert Eb/No from dB to linear scale
    noise_power = 1 / (2 * EbNo_lin)  # Calculate noise power based on Eb/No
    noise = np.sqrt(noise_power / 2) * (np.random.randn(num_symbols) + 1j * np.random.randn(num_symbols))  
    # Generate complex Gaussian noise with real and imaginary parts

    recieved_symbols = qpsk_symbols + noise  # Add noise to the QPSK transmitted symbols
    estimated_symbols = np.argmin(abs(recieved_symbols[:, np.newaxis] - constellation), axis=1)  
    # Detect the closest constellation point for each received symbol

    num_error = np.sum(estimated_symbols != symbols)  # Count the number of symbol errors
    BER.append(num_error / (2 * num_symbols))  # Calculate and store BER (divide by 2*num_symbols for bit-level BER)

BER_theory = 0.5 * erfc(np.sqrt(10**(EbNo_db_Range / 10)))  
# Theoretical BER for QPSK using complementary error function (erfc)

plt.figure()  # Create a new figure
plt.semilogy(EbNo_db_Range, BER, '-', label='Simulated BER', linewidth=5)  # Plot simulated BER in log scale
plt.semilogy(EbNo_db_Range, BER_theory, '-o', label='Theoretical BER')  # Plot theoretical BER in log scale
plt.xlabel("Eb/No dB (SNR)")  # Label x-axis as Eb/No in dB
plt.ylabel("BER")  # Label y-axis as BER
plt.legend()  # Add legend to distinguish between simulated and theoretical curves
plt.title("Error Probability of QPSK")  # Title of the plot
plt.grid()  # Enable grid for better visualization

plt.figure()  # Create a new figure
plt.plot(qpsk_symbols.real, qpsk_symbols.imag, 'o')  # Plot QPSK constellation points (real vs imaginary components)
plt.xlabel("In-Phase")  # Label x-axis as in-phase component
plt.ylabel("Quadrature")  # Label y-axis as quadrature component
plt.title("Constellation Diagram of QPSK")  # Title of the constellation diagram
plt.grid()  # Enable grid for better visualization

plt.show()  # Display all the plots

