import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# --- PARAMETERS ---
n = 5000  # number of rolls
seed = 50
random.seed(seed)
np.random.seed(seed)


# SIMULATION 
rolls = np.random.randint(1, 7, size=n)


# EMPIRICAL STATISTICS 
empirical_mean = rolls.mean()
empirical_var_sample = rolls.var(ddof=1)   # sample variance
empirical_var_pop = rolls.var(ddof=0)      # population variance


#THEORETICAL VALUES
theoretical_mean = 3.5
theoretical_var = 35/12   # 2.916666...


# ERRORS
abs_error_var = abs(empirical_var_sample - theoretical_var)
rel_error_var_pct = (abs_error_var / theoretical_var) * 100


# RESULTs
df = pd.DataFrame({
    "n_rolls": [n],
    "empirical_mean": [empirical_mean],
    "theoretical_mean": [theoretical_mean],
    "empirical_sample_variance": [empirical_var_sample],
    "empirical_population_variance": [empirical_var_pop],
    "theoretical_variance_35/12": [theoretical_var],
    "abs_error_variance": [abs_error_var],
    "relative_error_%": [rel_error_var_pct]
})


print(df)


# PLOTS
plt.figure(figsize=(10,4))


# Histogram of rolls
plt.subplot(1,2,1)
plt.hist(rolls, bins=np.arange(1,8)-0.5, edgecolor='black')
plt.axvline(empirical_mean, label="Empirical Mean")
plt.axvline(theoretical_mean, linestyle="--", label="Theoretical Mean = 3.5")
plt.xticks(np.arange(1,7))
plt.title("Histogram of Dice Rolls")
plt.xlabel("Outcome")
plt.ylabel("Frequency")
plt.legend(prop={'size': 5}, loc='upper right')








# Variance comparison bar plot
plt.subplot(1,2,2)
x = [0, 1]
plt.bar(x, [empirical_var_sample, theoretical_var], width=0.6)
plt.xticks(x, ["Empirical Var", "Theoretical Var"])
plt.ylabel("Variance")
plt.title("Sample vs Theoretical Variance")


plt.tight_layout()
plt.show()


