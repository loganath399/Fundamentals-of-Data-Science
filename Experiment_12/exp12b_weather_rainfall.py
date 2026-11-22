import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weather_data.csv")

plt.scatter(df["Month"], df["Rainfall"],
            color='blue', s=80)

plt.title("Monthly Rainfall")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()