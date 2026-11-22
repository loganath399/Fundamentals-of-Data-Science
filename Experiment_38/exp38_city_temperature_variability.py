import pandas as pd

# Load dataset
df = pd.read_csv("city_temperatures.csv")
cities = [col for col in df.columns if col != 'Day']

# 1. Mean temperature for each city
mean_temps = df[cities].mean()

# 2. Standard deviation of temperature for each city
std_temps = df[cities].std()

# 3. Temperature range (Max - Min)
temp_ranges = df[cities].max() - df[cities].min()
highest_range_city = temp_ranges.idxmax()

# 4. Most consistent temperature (lowest std dev)
most_consistent_city = std_temps.idxmin()

print("1. Mean Temperature (°C):")
print(mean_temps.round(2))

print("\n2. Standard Deviation (°C):")
print(std_temps.round(2))

print(f"\n3. City with Highest Temperature Range: {highest_range_city} ({temp_ranges[highest_range_city]:.2f}°C)")
print(f"4. City with Most Consistent Temperature: {most_consistent_city} (Std Dev: {std_temps[most_consistent_city]:.2f}°C)")
