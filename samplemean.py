import random
import matplotlib.pyplot as plt


# Number of rolls
n = 5000


# Simulate die rolls
rolls = [random.randint(1, 6) for _ in range(n)]


# Compute cumulative sample mean
cumulative_means = []
total = 0


for i, value in enumerate(rolls):
    total += value
    cumulative_means.append(total / (i + 1))


# Plot cumulative mean
plt.figure(figsize=(9, 5))
plt.plot(cumulative_means, label="Cumulative Sample Mean")


# Overlay theoretical mean (3.5)
plt.axhline(3.5, color='red', linestyle='--', label="Theoretical Mean = 3.5")


plt.xlabel("Number of Rolls")
plt.ylabel("Cumulative Mean")
plt.title("Convergence of Sample Mean Toward Expected Value (E[X] = 3.5)")
plt.legend()
plt.tight_layout()
plt.show()
