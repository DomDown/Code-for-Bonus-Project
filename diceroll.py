import random
import numpy as np
import matplotlib.pyplot as plt


# Simulate 10,000 rolls 
n = 10000
rolls = [random.randint(1, 6) for _ in range(n)]


#  Compute empirical frequencies 
empirical_counts = [rolls.count(face) for face in range(1, 7)]
empirical_rel_freq = [count / n for count in empirical_counts]


print("Empirical counts:", empirical_counts)
print("Empirical relative frequencies:", empirical_rel_freq)


#  Plot histogram 
plt.figure(figsize=(8, 5))
plt.hist(rolls, bins=np.arange(1, 8)-0.5, edgecolor="black", alpha=0.8)


# Theoretical probability: 1/6 
theoretical_prob = 1/6
x_vals = np.arange(1, 7)
theoretical_counts = [theoretical_prob * n] * 6


#  Overlay theoretical distribution 
plt.bar(x_vals, theoretical_counts, width=0.3, alpha=0.5, label="Theoretical Expected Count")


plt.xticks(x_vals)
plt.xlabel("Die Outcome")
plt.ylabel("Frequency")
plt.title("Histogram of 10,000 Simulated Die Rolls")


plt.legend(prop={'size': 8}, loc='upper right')


plt.tight_layout()
plt.show()
