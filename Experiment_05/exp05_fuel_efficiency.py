import numpy as np

fuel_efficiency = np.loadtxt(
    "fuel_efficiency.csv", delimiter=",",
    skiprows=1, usecols=1
)

average_efficiency = np.mean(fuel_efficiency)

car1 = fuel_efficiency[0]
car2 = fuel_efficiency[1]

percentage_improvement = (
    (car2 - car1) / car1
) * 100

print("Average Fuel Efficiency:",
      round(average_efficiency, 2), "MPG")

print("Percentage Improvement from Car_A to Car_B:",
      round(percentage_improvement, 2), "%")