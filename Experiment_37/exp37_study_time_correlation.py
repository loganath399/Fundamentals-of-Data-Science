import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("study_exam_scores.csv")

# Calculate Pearson correlation
corr = df['StudyHours'].corr(df['ExamScore'])
print(f"Correlation between Study Time and Exam Score: {corr:.4f}")

# Create multiple visualizations
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Scatter plot with trend
axes[0].scatter(df['StudyHours'], df['ExamScore'], color='teal', s=70)
axes[0].set_title(f"Study Hours vs Exam Score (r = {corr:.2f})")
axes[0].set_xlabel("Study Time (Hours)")
axes[0].set_ylabel("Exam Score")
axes[0].grid(True)

# Line plot
axes[1].plot(df['StudyHours'], df['ExamScore'], marker='o', color='coral')
axes[1].set_title("Score Progression by Study Time")
axes[1].set_xlabel("Study Time (Hours)")
axes[1].set_ylabel("Exam Score")
axes[1].grid(True)

plt.tight_layout()
plt.show()
