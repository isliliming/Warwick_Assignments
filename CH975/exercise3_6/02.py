import matplotlib.pyplot as plt
import numpy as np

# Function definition for Van der Waals potential
def w_vdw(D, R):
    term1 = -((1.4E-20)/6) * ((2 * R * R) / ((4 * R + D) * D))
    term2 = -((1.4E-20)/6) * (2 * R * R) / ((2 * R + D) * (2 * R + D))
    term3 = -((1.4E-20)/6) * np.log(((4 * R + D) * D) / ((2 * R + D) * (2 * R + D)))
    return term1 + term2 + term3

# Generate a range of D values
D = np.linspace(0, 1E-9, 100)

# Create the plot outside the loop
plt.figure(figsize=(10, 8))

# Define a list of line styles
line_styles = ['-', '--', '-.', ':']

# Define a list of markers
markers = ['o', 's', '^', 'd', 'x', '+']

# Loop over the different values of R
for i, R in enumerate([1E-9, 10E-9, 50E-9, 100E-9, 200E-9, 1000E-9]):
    vdw_values = w_vdw(D, R)
    # Cycle through line_styles and markers using modulus to avoid index error
    line_style = line_styles[i % len(line_styles)]
    marker = markers[i % len(markers)]
    plt.plot(D, vdw_values, label=f'R = {R:.0e} m', linestyle=line_style, marker=marker, markevery=5)

# Enhance the plot
plt.title('Van der Waals Potential vs. Distance for Different Radii', fontsize=16)
plt.xlabel('Distance (m)', fontsize=14)
plt.ylabel('Potential Energy (J)', fontsize=14)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.tight_layout()  # Adjust the padding between and around subplots.

# Set the x and y axis limits if necessary
plt.xlim([0, 1E-9])
# For y-axis, we find the global minimum and maximum across all R values
all_vdw_values = [w_vdw(D, R) for R in [1E-9, 10E-9, 50E-9, 100E-9, 200E-9, 1000E-9]]
plt.ylim([min(map(min, all_vdw_values)), max(map(max, all_vdw_values))])

# Save the figure to a file
#plt.savefig('van_der_waals_plot.png', dpi=300)

# Show the plot
plt.show()
