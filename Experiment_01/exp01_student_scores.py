import numpy as np

student_scores = np.loadtxt(
    "student_scores.csv", delimiter=",", skiprows=1
)

subjects = ["Math", "Science", "English", "History"]

average_scores = np.mean(student_scores, axis=0)

print("Average Score of Each Subject:")
for i in range(len(subjects)):
    print(subjects[i], ":", round(average_scores[i], 2))

highest = np.argmax(average_scores)
print("Subject with Highest Average:", subjects[highest])