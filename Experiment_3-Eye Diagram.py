# Import necessary libraries
import numpy as np             # For numerical operations and array handling
import matplotlib.pyplot as plt # For plotting the graphs
from scipy.signal import upfirdn  # For upsampling and filtering

# Define parameters for the simulation
N = 100          # Number of symbols in the data sequence
span = 10        # The span of the filter in symbol periods
sps = 8          # Number of samples per symbol (sampling rate)
rolloff = 0.4    # Roll-off factor for the raised cosine filter (defines the bandwidth)

# Function to create a raised cosine filter (used for pulse shaping)
def rsed_cos(rolloff, span, sps):
    # Create a time vector 't' that spans from -span/2 to span/2 with sps*span points
    t = np.linspace(-span/2, span/2, sps*span)
    
    # Initialize an array 'response' to store the filter's impulse response
    response = np.zeros(sps*span)
    
    # Loop through each point in the time vector and compute the filter response
    for i in range(sps*span):
        # Special case for the singularity when abs(t) == span/(2*rolloff)
        if abs(t[i]) == (span/(2*rolloff)):
            # Use a special formula to avoid division by zero
            response[i] = np.sinc(span/(2*rolloff)) * np.pi / 4
        else:
            # Compute the raised cosine filter using the sinc function and the cosine term
            response[i] = np.sinc(t[i]) * np.cos(np.pi * rolloff * t[i] / span) / (1 - (2 * rolloff * t[i] / span)**2)
    
    # Return the computed filter response
    return response

# Generate a random sequence of N symbols (each symbol is either -1 or 1)
data = np.random.choice([-1, 1], size=N)

# Generate the raised cosine filter using the defined function
rct_filt = rsed_cos(rolloff, span, sps)

# Upsample the data by a factor of 10 and filter it using the raised cosine filter
# The 'upfirdn' function performs upsampling and filtering
UP_s = upfirdn(rct_filt, data, up=10)

# Plot the baseband signal after pulse shaping
plt.figure()  # Create a new figure for the plot
plt.plot(UP_s)  # Plot the upsampled and filtered signal
plt.title("Baseband Signal")  # Set the title of the plot
plt.grid()  # Enable grid for better readability

# Create a new figure for the eye diagram
plt.figure()  
for i in range(N):
    # Plot segments of the upsampled signal corresponding to each symbol (shifted by 10 samples for each symbol)
    # This creates a visual representation of the signal over multiple symbol intervals
    plt.plot(UP_s[i*10:(i+2)*10], linewidth=0.6)  # Plot a short segment of the signal
plt.title("Eye Diagram")  # Set the title of the plot
plt.grid()  # Enable grid for better readability

# Display the plots
plt.show()  # Show all the generated plots

