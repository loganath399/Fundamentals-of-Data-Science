import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weather_data.csv")

plt.plot(df["Month"], df["Temperature"],
         marker='o', color='orange')

plt.title("Monthly Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (Celsius)")
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()