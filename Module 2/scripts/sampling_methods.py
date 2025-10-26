import numpy as np
import pandas as pd


# Create a diverse population
np.random.seed(42)
pop_data = pd.DataFrame({
    "customer_id": range(1, 5001),
    "age": np.random.normal(40, 15, 5000).clip(18, 85),
    "income": np.random.lognormal(11, 0.5, 5000),
    "region": np.random.choice(['North', 'South', 'East', 'West'], 5000, p=[0.3, 0.25, 0.25, 0.2])
})

print("=== POPULATION CHARACTERISTICS ===")
print(pop_data.groupby('region').agg({"income": ['count', 'mean', 'std']}))

# Method 1: Simple Random Sampling
srs_sample = pop_data.sample(n=500, random_state=42)
print("\n=== SIMPLE RANDOM SAMPLE (n=500) ===")
print(f"Mean income: ${srs_sample['income'].mean():,.2f}")
print(f"Regional distribution:\n{srs_sample['region'].value_counts()}")

# Method 2: Stratified Random Sampling
# Ensure proportional representation by region
stratified_sample = pop_data.groupby('region', group_keys=False).apply(
    lambda x: x.sample(frac=0.1, random_state=42)
)

print("\n=== STRATIFIED RANDOM SAMPLE (10% from each region) ===")
print(f"Mean income: ${stratified_sample['income'].mean():,.2f}")
print(f"Regional distribution:\n{stratified_sample['region'].value_counts()}")

# Compare sampling error
true_mean = pop_data['income'].mean()
srs_error = abs(srs_sample['income'].mean() - true_mean)
stratified_error =abs(stratified_sample['income'].mean() - true_mean)

print("\n=== SAMPLING ERROR COMPARISON ===")
print(f"True population mean: ${true_mean:,.2f}")
print(f"SRS Error: ${srs_error:,.2f}")
print(f"Stratified error: ${stratified_error:,.2f}")

# Demonstrate with/without replacement
n_simulations = 1000
sample_size = 100

with_replacement_means = []
without_replacement_means = []

for _ in range(n_simulations):
    with_repl = pop_data['income'].sample(n=sample_size, replace=True)
    without_repl = pop_data['income'].sample(n=sample_size, replace=False)
    
    with_replacement_means.append(with_repl.mean())
    without_replacement_means.append(without_repl.mean())
    
print(f"\n=== WITH vs. WITHOUT REPLACEMENT ===")
print(f"With replacement - SE: ${np.std(with_replacement_means, ddof=1):,.2f}")
print(f"Without replacement - SE: ${np.std(without_replacement_means, ddof=1):,.2f}")
print(f"Difference: Negligible for large population")