import pandas as pd
import matplotlib.pyplot as plt

# Read social media dataset
df = pd.read_csv("social_media.csv")

# Calculate frequency distribution
frequency = df["Likes"].value_counts().sort_index()

# Display frequency
print("Frequency Distribution of Likes")
print("--------------------------------")
print(frequency)

# Create bar plot
plt.bar(frequency.index, frequency.values,
        color='purple')

plt.title("Frequency Distribution of Post Likes")
plt.xlabel("Number of Likes")
plt.ylabel("Number of Posts")
plt.grid(axis='y')
plt.show()