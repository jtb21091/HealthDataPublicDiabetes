# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the newly uploaded dataset
file_path = "Datasets/DiabetesAtlas_NationalData (1).csv"  # Update this with the correct file path
df = pd.read_csv(file_path, skiprows=10, engine='python')

# Rename columns for clarity
df.columns = ['Year', 'Rate per 1000', 'Unused1', 'Unused2', 'Unused3']
df = df[['Year', 'Rate per 1000']]  # Keep only necessary columns

# Convert numeric columns to proper data types
df['Rate per 1000'] = pd.to_numeric(df['Rate per 1000'], errors='coerce')

# Remove the last row
df = df.iloc[:-1]

# Calculate total sum of the 'Rate per 1000' column
sum_total = df['Rate per 1000'].sum()
print(f"Total Sum Across All Years: {sum_total}")

# Calculate yearly totals
yearly_totals = df[['Year', 'Rate per 1000']]
print("Yearly Totals:")
print(yearly_totals)

# Plot the yearly totals
plt.figure(figsize=(10, 5))
plt.bar(df['Year'], df['Rate per 1000'], color='blue')
plt.xlabel('Year')
plt.ylabel('Rate per 1000')
plt.title('Diabetes Incidence Rate per 1000 Over the Years')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save the plot as a PNG file in the specified folder
plt.savefig("pngfiles/rate_per_1000_trend.png", dpi=300, bbox_inches='tight')
plt.show()

print("Plot saved as 'pngfiles/rate_per_1000_trend.png'")
