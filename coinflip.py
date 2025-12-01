import random
import matplotlib.pyplot as plt


# Choose 6 different values of n 
n_values = [10, 50, 100, 500, 1000, 2000]


plt.figure(figsize=(10, 6))


for n in n_values:
    heads_count = 0
    relative_frequency = []


    # Run the simulation for each n
    for i in range(1, n + 1):
        flip = random.choice(["H", "T"])
        if flip == "H":
            heads_count += 1
        relative_frequency.append(heads_count / i)
   
    # Plot this run
    plt.plot(range(1, n + 1), relative_frequency, label=f"n = {n}")


# Add theoretical 0.5 line
plt.axhline(0.5, color="black", linestyle="--", label="Theoretical = 0.5")


plt.xlabel("Number of Flips")
plt.ylabel("Relative Frequency of Heads")
plt.title("Relative Frequency of Heads for Multiple Values of n")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
