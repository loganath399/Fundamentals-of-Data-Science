import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Read CSV file
df = pd.read_csv("treatment.csv")

# Separate groups
treatment = df[df['Group'] == 'Treatment']['Reduction']
control = df[df['Group'] == 'Control']['Reduction']

# Independent t-test
t_stat, p_value = stats.ttest_ind(
    treatment, control, equal_var=False
)

print("Treatment Mean:", treatment.mean())
print("Control Mean:", control.mean())
print("T-statistic:", t_stat)
print("P-value:", p_value)

if p_value < 0.05:
    print("Treatment has a significant effect")
else:
    print("No significant effect")

# Visualization
plt.bar(
    ['Treatment', 'Control'],
    [treatment.mean(), control.mean()]
)
plt.title(f"Treatment Effectiveness (p-value = {p_value:.2e})")
plt.ylabel("Mean Reduction")
plt.show()
