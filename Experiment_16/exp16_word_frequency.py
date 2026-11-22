import pandas as pd
import re
from collections import Counter

# Read CSV file
df = pd.read_csv("reviews.csv")

# Combine reviews
text = " ".join(df['Review'].astype(str))

# Convert to lowercase
text = text.lower()

# Extract words
words = re.findall(r'\b[a-z]+\b', text)

# Calculate frequency
frequency = Counter(words)

print("Word Frequency Distribution")
for word, count in frequency.items():
    print(word, ":", count)
