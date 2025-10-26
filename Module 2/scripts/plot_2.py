from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create dataset with missing data
np.random.seed(42)
n = 1000

data_complete = pd.DataFrame({
    'age': np.random.normal(40, 12, n),
    'income': np.random.normal(60000, 20000, n),
    'education': np.random.choice(['HS', 'BA', 'MA', 'PhD'], n, p=[0.3, 0.4, 0.2, 0.1])
})

# Introduce missingness - MCAR for age
mcar_mask = np.random.random(n) < 0.10
data_complete.loc[mcar_mask, 'age'] = np.nan

# Introduce missingness - MAR for income (depends on education)
mar_prob = data_complete['education'].map({'HS': 0.20, 'BA': 0.10, 'MA': 0.05, 'PhD': 0.02})
mar_mask = np.random.random(n) < mar_prob
data_complete.loc[mar_mask, 'income'] = np.nan

# Introduce missingness - MNAR for income (high earners don't report)
mnar_mask = (data_complete['income'] > 85000) & (np.random.random(n) < 0.30)
data_complete.loc[mnar_mask, 'income'] = np.nan

data_missing = data_complete.copy()

print("=== MISSING DATA SUMMARY ===")
print(data_missing.isnull().sum())
print(f"\nPercentage missing:")
print((data_missing.isnull().sum() / len(data_missing) * 100).round(2))

# Analyze missingness patterns
print("\n=== MISSINGNESS PATTERN ===")
print(data_missing.groupby('education')['income'].apply(lambda x: x.isnull().sum()))

# Method 1: Listwise deletion
data_complete_cases = data_missing.dropna()
print(f"\n=== LISTWISE DELETION ===")
print(f"Original sample size: {len(data_missing)}")
print(f"After deletion: {len(data_complete_cases)} ({100*len(data_complete_cases)/len(data_missing):.1f}%)")

# Method 2: Mean imputation
imputer_mean = SimpleImputer(strategy='mean')
data_mean_imputed = data_missing.copy()
data_mean_imputed[['age', 'income']] = imputer_mean.fit_transform(data_missing[['age', 'income']])

print(f"\n=== MEAN IMPUTATION ===")
print(f"Imputed age mean: {data_mean_imputed['age'].mean():.2f}")
print(f"Imputed income mean: ${data_mean_imputed['income'].mean():,.2f}")

# Method 3: K-NN Imputation
# Need to encode categorical first
data_encoded = data_missing.copy()
data_encoded = pd.get_dummies(data_encoded, columns=['education'], drop_first=False)

imputer_knn = KNNImputer(n_neighbors=5)
data_knn_imputed = pd.DataFrame(
    imputer_knn.fit_transform(data_encoded),
    columns=data_encoded.columns
)

print(f"\n=== K-NN IMPUTATION ===")
print(f"Imputed age mean: {data_knn_imputed['age'].mean():.2f}")
print(f"Imputed income mean: ${data_knn_imputed['income'].mean():,.2f}")

# Method 4: Multiple Imputation (MICE)
imputer_mice = IterativeImputer(random_state=42, max_iter=10)
data_mice_imputed = data_missing.copy()
data_mice_imputed[['age', 'income']] = imputer_mice.fit_transform(data_missing[['age', 'income']])

print(f"\n=== MICE (MULTIPLE IMPUTATION) ===")
print(f"Imputed age mean: {data_mice_imputed['age'].mean():.2f}")
print(f"Imputed income mean: ${data_mice_imputed['income'].mean():,.2f}")

# Compare to true values (before introducing missingness)
print(f"\n=== COMPARISON TO TRUE VALUES ===")
print(f"True age mean: {data_complete['age'].mean():.2f}")
print(f"True income mean: ${data_complete['income'].mean():,.2f}")

# Visualize impact of missing data
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

axes[0].hist(data_complete['income'].dropna(), bins=30, alpha=0.5, label='Complete', density=True)
axes[0].hist(data_complete_cases['income'], bins=30, alpha=0.5, label='After Deletion', density=True)
axes[0].set_title('Listwise Deletion Impact')
axes[0].set_xlabel('Income')
axes[0].legend()

axes[1].hist(data_complete['income'].dropna(), bins=30, alpha=0.5, label='Complete', density=True)
axes[1].hist(data_mean_imputed['income'], bins=30, alpha=0.5, label='Mean Imputed', density=True)
axes[1].set_title('Mean Imputation Impact')
axes[1].set_xlabel('Income')
axes[1].legend()

axes[2].hist(data_complete['income'].dropna(), bins=30, alpha=0.5, label='Complete', density=True)
axes[2].hist(data_knn_imputed['income'], bins=30, alpha=0.5, label='KNN Imputed', density=True)
axes[2].set_title('KNN Imputation Impact')
axes[2].set_xlabel('Income')
axes[2].legend()

plt.tight_layout()
plt.show()