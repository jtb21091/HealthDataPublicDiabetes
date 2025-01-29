# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "Datasets/DiabetesAtlas_NationalData.csv"  # Update this with the correct file path
df = pd.read_csv(file_path, skiprows=10, engine='python')

# Rename columns for clarity
df.columns = ['Year', 'Diagnosed %', 'Lower_Bound', 'Upper_Bound', 'Unused']
df = df.drop(columns=['Unused'])  # Remove unnecessary column

# Convert numeric columns to proper data types
df[['Diagnosed %', 'Lower_Bound', 'Upper_Bound']] = df[['Diagnosed %', 'Lower_Bound', 'Upper_Bound']].apply(pd.to_numeric, errors='coerce')

# Remove the last row
df = df.iloc[:-1]

# Calculate total sum of the 'Diagnosed %' column
sum_total = df['Diagnosed %'].sum()
print(f"Total Sum Across All Years: {sum_total}")

# Calculate yearly totals
yearly_totals = df[['Year', 'Diagnosed %']]
print("Yearly Totals:")
print(yearly_totals)

# Plot the yearly totals
plt.figure(figsize=(10, 5))
plt.bar(df['Year'], df['Diagnosed %'], color='blue')
plt.xlabel('Year')
plt.ylabel('Diagnosed %')
plt.title('Diabetes Trends Over the Years')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save the plot as a PNG file in the specified folder
plt.savefig("pngfiles/diabetes_trend.png", dpi=300, bbox_inches='tight')
plt.show()

print("Plot saved as 'pngfiles/diabetes_trend.png'")
