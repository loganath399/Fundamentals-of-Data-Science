import pandas as pd
import matplotlib.pyplot as plt
import re
from collections import Counter
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

# Read CSV file
df = pd.read_csv("data.csv")

# Combine feedback
text = " ".join(df['feedback'].astype(str)).lower()

# Remove punctuation
words = re.findall(r'\b[a-z]+\b', text)

# Remove stop words
words = [w for w in words if w not in ENGLISH_STOP_WORDS]

# Calculate frequency
frequency = Counter(words)

# Get top N words
n = int(input("Enter number of top words: "))
top_words = frequency.most_common(n)

print("\nTop Frequent Words")
for word, count in top_words:
    print(word, ":", count)

# Bar graph
if top_words:
    labels, values = zip(*top_words)
    plt.bar(labels, values)
    plt.title("Top N Frequent Words")
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.show()
