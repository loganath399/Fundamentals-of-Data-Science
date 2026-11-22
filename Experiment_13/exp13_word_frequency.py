import re
from collections import Counter

# Read text file
with open("sample_text.txt", "r") as file:
    text = file.read()

# Convert to lowercase
text = text.lower()

# Extract words
words = re.findall(r'\b[a-z]+\b', text)

# Calculate word frequency
frequency = Counter(words)

# Display output
print("Word Frequency Distribution")


for word, count in sorted(frequency.items()):
    print(word, ":", count)