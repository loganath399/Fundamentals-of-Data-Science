import pandas as pd
import matplotlib.pyplot as plt

# Read dataset from CSV
df = pd.read_csv("soccer_players.csv")

# Top 5 players with highest goals scored
top_goals = df.nlargest(5, 'GoalsScored')[['Name', 'Position', 'GoalsScored']]
print("--- Top 5 Players by Goals Scored ---")
print(top_goals.to_string(index=False))

# Top 5 players with highest weekly salaries
top_salaries = df.nlargest(5, 'WeeklySalary')[['Name', 'Position', 'WeeklySalary']]
print("\n--- Top 5 Players by Weekly Salary ---")
print(top_salaries.to_string(index=False))

# Average age and players above average age
avg_age = df['Age'].mean()
above_avg_players = df[df['Age'] > avg_age][['Name', 'Age']]
print(f"\nAverage Age of Players: {avg_age:.2f} years")
print("--- Players Above Average Age ---")
print(above_avg_players.to_string(index=False))

# Bar chart of player distribution by position
position_counts = df['Position'].value_counts()
plt.figure(figsize=(8, 5))
position_counts.plot(kind='bar', color='steelblue', edgecolor='black')
plt.title("Distribution of Soccer Players by Position")
plt.xlabel("Position")
plt.ylabel("Number of Players")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
