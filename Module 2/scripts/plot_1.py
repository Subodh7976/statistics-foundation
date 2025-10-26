import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.random.seed(42)
POPULATION_SIZE = 100000

# Create a population with known parameters
population = pd.DataFrame({
    'age': np.random.normal(loc=45, scale=15, size=POPULATION_SIZE).clip(18, 90),
    'income': np.random.lognormal(mean=10.8, sigma=0.6, size=POPULATION_SIZE)
})

# True population parameters (what we'd know if we could measure everyone)
mu_age = population['age'].mean()
mu_income = population['income'].mean()
sigma_age = population['age'].std(ddof=0) # Population std
sigma_income = population['income'].std(ddof=0)

print("=== TRUE POPULATION PARAMETERS ===")
print(f"Population size (N): {POPULATION_SIZE:,}")
print(f"mu (age): {mu_age:.2f} years")
print(f"mu (income): ${mu_income:.2f}")
print(f"sigma (age): {sigma_age:.2f}")
print(f"sigma (income): ${sigma_income:.2f}")

# Draw a sample
SAMPLE_SIZE = 500
sample = population.sample(n=SAMPLE_SIZE, random_state=42)

# Sample statistics (estimates)
x_bar_age = sample['age'].mean()
x_bar_income = sample['income'].mean()
s_age = sample['age'].std(ddof=1) # Sample std (with Bessel's correction)
s_income = sample['income'].std(ddof=1)

print("\n=== SAMPLE STATISTICS ===")
print(f"Sample size (n): {SAMPLE_SIZE}")
print(f"x_bar (age): {x_bar_age:.2f} years")
print(f"x_bar (income): ${x_bar_income:.2f}")
print(f"s (age): {s_age:.2f}")
print(f"s (income): ${s_income:.2f}")

print("\n=== SAMPLING ERROR ===")
print(f"Error in age mean: {x_bar_age - mu_age:.2f} years ({100*(x_bar_age - mu_age)/mu_age:.2f}%)")
print(f"Error in income mean: ${x_bar_income - mu_income:,.2f} ({100*(x_bar_income - mu_income)/mu_income:.2f}%)")

# Demonstrate sampling distribution
n_samples = 1000
sample_means_age = []
sample_means_income = []

for _ in range(n_samples):
    temp_sample = population.sample(n=SAMPLE_SIZE)
    sample_means_age.append(temp_sample['age'].mean())
    sample_means_income.append(temp_sample['income'].mean())

# Standard error (empirical vs. theoretical)
se_age_empirical = np.std(sample_means_age, ddof=1)
se_age_theoretical = sigma_age / np.sqrt(SAMPLE_SIZE)

print("\n=== STANDARD ERROR (Age) ===")
print(f"Empirical SE: {se_age_empirical:.3f}")
print(f"Theoretical SE (sigma/n^1/2): {se_age_theoretical:.3f}")
print(f"Close match validates Central Limit Theorem")

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].hist(population['age'], bins=50, alpha=0.5, label='Population', density=True, color='blue')
axes[0].hist(sample['age'], bins=30, alpha=0.7, label=f'Sample (n={SAMPLE_SIZE})', density=True, color='orange')
axes[0].axvline(mu_age, color='blue', linestyle='--', linewidth=2, label=f'μ = {mu_age:.1f}')
axes[0].axvline(x_bar_age, color='orange', linestyle='--', linewidth=2, label=f'x̄ = {x_bar_age:.1f}')
axes[0].set_xlabel('Age')
axes[0].set_ylabel('Density')
axes[0].set_title('Population vs. Sample Distribution (Age)')
axes[0].legend()

axes[1].hist(sample_means_age, bins=40, alpha=0.7, color='green', edgecolor='black')
axes[1].axvline(mu_age, color='red', linestyle='--', linewidth=2, label=f'True μ = {mu_age:.1f}')
axes[1].set_xlabel('Sample Mean (Age)')
axes[1].set_ylabel('Frequency')
axes[1].set_title(f'Sampling Distribution of Mean\n({n_samples} samples of size {SAMPLE_SIZE})')
axes[1].legend()

plt.tight_layout()
plt.show()