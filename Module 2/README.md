
## Primary vs Secondary Data Sources

| Aspect             | Primary Data                                                                           | Secondary Data                                                                                    |
| ------------------ | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Definition         | Original data collected for specific research question                                 | Pre-existing data collected by others                                                             |
| Control            | Full control over collection methodology                                               | No control over original methodology                                                              |
| Relevance          | Perfectly tailored to research needs                                                   | May require adaptation or transformation                                                          |
| Cost               | Higher (time, resources, effort)                                                       | Lower (already available)                                                                         |
| Time               | Longer to collect                                                                      | Immediate availability                                                                            |
| Quality assurance  | Direct Oversight                                                                       | Depends on original source reliability                                                            |
| Collection methods | Surveys & questionnaires, Experiments, Observations, Interviews, Sensors & Instruments | Government databases, Academic datasets, Commercial data, Open data, Internal organizational data |

---

## Population vs Sample

#### Philosophical Foundations
The **Population** represents the complete set of all possible observations about which we wish to draw conclusions. The **Sample** is a subset drawn from this population for practical study.

Let $P$ denote a population with size $N$. A sample $S \subset P$ contains $n$ observations, where $n \ll N$.

**Key Distinctions**

| Concept            | Population                                 | Sample                             |
| ------------------ | ------------------------------------------ | ---------------------------------- |
| Symbol for size    | $N$                                        | $n$                                |
| Mean symbol        | $\mu$                                      | $\bar x$                           |
| Standard deviation | $\sigma$                                   | $s$                                |
| Variance           | $\sigma^2$                                 | $s^2$                              |
| Proportion         | $\pi$ or $p$                               | $\hat p$                           |
| Nature             | Fixed (though often unknown) parameter     | Random variable (varies by sample) |
| Accessibility      | Often impractical or impossible to measure | Feasible to observe and measure    |

**The Inference Problem**
Statistics fundamentally addresses the problem of inductive inference: How can we make valid generalizations about $P$ based only on observations from $S$?
The relation between sample statistics and population parameters:
$$
\text{Sample Statistic = Population Parameter + Sampling Error}
$$
For example, the sample mean:
$$
\bar x = \mu + \epsilon
$$
where $\epsilon$ represents sampling error - the random deviation due to observing only a subset of the population.

#### Three Types of Populations

1. **Finite, enumerable populations:** All U.S. registered voters, all Fortune 500 companies.
2. **Finite, but practically infinite:** All adult humans on Earth (7+ billion)
3. **Conceptual/Infinite populations:** All possible coin flips, all future customers, all potential measurements.
The third type is **theoretical** - it represents not just existing observations but all possible observations under similar conditions.

Example: 
```text
=== TRUE POPULATION PARAMETERS ===
Population size (N): 100,000
μ (age): 45.22 years
μ (income): $58681.83
σ (age): 14.52
σ (income): $38382.48

=== SAMPLE STATISTICS ===
Sample size (n): 500
x̄ (age): 45.95 years
x̄ (income): $57774.87
s (age): 14.68
s (income): $36596.64

=== SAMPLING ERROR ===
Error in age mean: 0.72 years (1.60%)
Error in income mean: $-906.97 (-1.55%)

=== STANDARD ERROR (Age) ===
Empirical SE: 0.637
Theoretical SE (σ/√n): 0.649
Close match validates Central Limit Theorem
```

#### Why We Sample Instead of Measuring Everything

**Fundamental Rationale**
A census - measuring every member of the population - seems ideal but is often impractical or impossible. Reasons for Sampling - Cost Efficiency, Time Constraints, Destructive Testing, Inaccessible Populations, Accuracy Paradox.

**The Quality vs Quantity Trade-Off**
**George Gallup's insight (1936):** A carefully selected sample of 2,000 voters predicted the U.S. presidential election accurately, while the Literary Digest's survey of 10 million voters - biased toward affluent individuals - failed spectacularly.

**Key Principle:** $\text{Data Quality > Data Quantity}$ 

> The **standard error** of a sample mean decreases with the square root of sample size:

$$
SE(\bar x) = \frac{\sigma}{\sqrt{n}}
$$
To halve the error -> **the sample size must be quadruple.**

**When is a census Appropriate?**
- Small, accessible populations (e.g., all employees in a small company)
- Legal/regulatory requirements (e.g., national census every 10 years)
- Administrative completeness needed (e.g., university enrollment records)

![[./plots/plot_1.png]]

#### Sampling Error vs Non-Sampling Error

**Sampling Error:** Natural variability due to observing only part of the population - **unavoidable but quantifiable.**
$$
\text{Sampling Error } \propto \frac{1}{\sqrt{n}}
$$

**Non-Sampling Error:** Mistakes in measurement, data entry, non-response, instrument calibration - can be large even in a census.

---

## Sampling: Random Sampling and Core Principles

#### Simple Random Sampling (SRS)

Each member of the population has an equal probability of being selected, and selections are independent.
Mathematically, if population size is $N$ and sample size is $n$:
$$
\text{P(any specific unit selected)} = \frac{n}{N}
$$
**Properties:**
- Unbiased: $E[\bar x]=\mu$
- Each possible sample of size $n$ has equal probability of selection
- Requires a sample frame: complete list of population members

#### Sampling With vs Without Replacement

**With replacement:** After selection, element is returned to population (can be selected again)
$$
\text{P(selection at draw k)} = \frac{1}{N} \hspace{1cm} \forall k
$$
**Without replacement:** Once selected, element is removed from pool.
$$
\text{P(selection at draw k|previous selections)} = \frac{1}{N - (k - 1)}
$$
#### Stratified Random Sampling

Population is divided into homogeneous subgroups (strata), and random samples are drawn from each stratum. 

**When to use:**
- Population has distinct subgroups with different characteristics. 
- Want to ensure representation of all groups.
- Need more precise estimates for specific subgroups
**Advantages:**
- Reduced sampling error compared to simple random sampling.
- Guaranteed representation of all strata.
- Enables subgroup analysis

$$
\bar x_{stratified} = \sum^H_{h=1}W_h \bar x_h
$$
where $W_h = N_h/N$ is the weight of stratum $h$, and $\bar x_h$ is the mean of stratum $h$.

**Example:** (*sampling_methods.py*)
```text
=== POPULATION CHARACTERISTICS ===
       income                            
        count          mean           std
region                                   
East     1236  69264.972956  35706.331848
North    1477  67516.023453  38348.315555
South    1275  67347.661470  36499.585751
West     1012  66546.631705  35005.396575

=== SIMPLE RANDOM SAMPLE (n=500) ===
Mean income: $65,584.49
Regional distribution:
region
North    157
East     119
South    118
West     106
Name: count, dtype: int64

=== STRATIFIED RANDOM SAMPLE (10% from each region) ===
Mean income: $67,094.93
Regional distribution:
region
North    148
South    128
East     124
West     101
Name: count, dtype: int64

=== SAMPLING ERROR COMPARISON ===
True population mean: $67,709.23
SRS Error: $2,124.73
Stratified error: $614.29

=== WITH vs. WITHOUT REPLACEMENT ===
With replacement - SE: $3,569.09
Without replacement - SE: $3,698.18
Difference: Negligible for large population
```

---

## Selection Bias and Its Real-World Consequences

**Selection Bias** occurs when the sample is systematically different from the population in ways that affect the conclusions. This creates systematic error that cannot be corrected by increasing sample size. 

#### The Literary Digest Debacle (1936)

**Context:** Literary Digest polled 10 million people and predicted Alf Landon would defeat Franklin Roosevelt. George Gallup polled 2,000 and correctly predicted Roosevelt's victory.

**The problem:** Literary Digest sample from:
- Their own subscribers (affluent)
- Telephone directories (luxury in 1936)
- Automobile registration lists (expensive)

**Result:** Sample bias - the sample over-represented wealthy voters who favored Landon.
$$
\text{Biased Estimate = True Parameter + Systematic Error + Random Error}
$$

Unlike random error, systematic error does not average out with larger samples.

#### Self-Selection Bias

Individuals choose whether to participate, creating non-randomness.
**Example:** Online Restaurant reviews (Yelp, Google)
- People with extreme experiences (very good or very bad) are more motivated to review
- Silent majority with average experiences under-represented
- Result: Biased toward extremes

#### Survivorship Bias

Focusing only on "survivors" and ignoring those that didn't make it.
**Example:** WWII aircraft armor placement.
- Military analyzed bullet holes in returning planes.
- Initially wanted to reinforce those areas.
- Flaw: Planes shot in critical areas didn't return - sampling only survivors!
- Correct action: Reinforce areas with no bullet holes.

#### Data Snooping and the Vast Search Effect

**Data Snooping:** Extensively searching through data until finding a pattern - but is it real or random?

**The vast search effect:** With enough variables and enough models, you'll always find something that looks significant by chance alone.

**Metaphor:** If 20,000 people each flip a coin 10 times, someone will get 10 heads. This doesn't mean they have special coin-flipping talent - it's probability.

**Probability of at least one person getting 10 heads:**
$$
P(\text{at least one success}) = 1 - P(\text{all fail}) = 1-(1-\frac{1}{1024})^{20000} \approx 0.9999
$$
**Mitigation Strategies:**
1. **Holdout validation sets:** Test findings on new, unseen data
2. **Cross-validation:** Multiple validation rounds
3. **Preregistration:** Specify hypothesis before data analysis
4. **Bonferroni correction:** Adjust significance levels for multiple comparisons
5. **Target shuffling:** Permutation tests to validate associations

---

## Missing Data

**Missing data** is ubiquitous in real-world datasets and can severely compromise analysis if handled improperly. Understanding why data is missing is as important as how much is missing.

#### Three Mechanisms of Missingness (Rubin's Taxonomy)

1. **Missing Completely at Random (MCAR)**
	- Missingness is independent of both observed and unobserved data
	- **Example:** Lab equipment randomly fails, affecting random observations
	- **Impact:** Reduces sample size but doesn't bias estimates
	- **Mathematical:** $P(M=1|X,Y) = P(M=1)$ 

2. **Missing at Random (MAR)**
	- Missingness depends on observed data, but not on the missing value itself
	- **Example:** Older people less likely to report income, but missingness explained by age
	- **Impact:** Can be corrected using observed variables
	- **Mathematical:** $P(M=1|X,Y) = P(M=1|X)$ 

3. **Missing not at Random (MNAR)**
	- Missingness depends on the unobserved (missing) value itself
	- **Example:** High earners refuse to disclose income
	- **Impact:** Creates bias; hardest to handle
	- **Mathematical:** $P(M=1|X,Y) = f(Y)$ 

**Consequences:**
1. **Reduced Statistical Power:** Smaller effective sample size increases standard errors.
2. **Biased Estimates:** If missingness is not random, parameters are systematically wrong
3. **Loss of Representativeness:** Complete-case analysis may not reflect population
4. **Reduced Generalizability:** Findings may not apply to groups with high missingness

#### Strategies for Handling Missing Data

| Method                 | Description                             | When Appropriate            | Limitations                             |
| ---------------------- | --------------------------------------- | --------------------------- | --------------------------------------- |
| Listwise deletion      | Remove any rows with missing data       | MCAR; large sample          | Loses information; can introduce bias   |
| Mean/median imputation | Replace missing with mean/median        | MCAR; descriptive analysis  | Reduce variance; distorts distributions |
| Mode imputation        | Replace missing categorical with mode   | MCAR; categorical data      | Oversimplifies; ignores relationships   |
| Regression imputation  | Predict missing values using regression | MAR; relationships exist    | Underestimates variability              |
| Multiple imputation    | Create multiple plausible datasets      | MAR; preserves uncertainity | Computationally intensive               |
| K-NN imputation        | Use similar records' values             | MAR; complex relationships  | Sensitive to scaling; slow              |
| Model-based methods    | Incorporate missingness in model        | Sophisticated analysis      | Requires strong assumptions             |

**Example:** (**plot_2.py**)
```text
=== MISSING DATA SUMMARY ===
age          109
income       140
education      0
dtype: int64

Percentage missing:
age          10.9
income       14.0
education     0.0
dtype: float64

=== MISSINGNESS PATTERN ===
education
BA     37
HS     79
MA     21
PhD     3
Name: income, dtype: int64

=== LISTWISE DELETION ===
Original sample size: 1000
After deletion: 764 (76.4%)

=== MEAN IMPUTATION ===
Imputed age mean: 40.22
Imputed income mean: $60,112.76

=== K-NN IMPUTATION ===
Imputed age mean: 40.16
Imputed income mean: $59,763.78

=== MICE (MULTIPLE IMPUTATION) ===
Imputed age mean: 40.22
Imputed income mean: $60,112.76

=== COMPARISON TO TRUE VALUES ===
True age mean: 40.22
True income mean: $60,112.76
```

![[./plots/plot_2.png]]

---

## Data Quality: Completeness, Consistency, and Accuracy

**Dimensions of Data Quality**
Data quality in data science extends beyond traditional statistical notions of representativeness:
1. **Completeness:** Are all required fields present? Minimal missingness?
2. **Consistency:** Do values conform to expected formats and ranges?
3. **Accuracy:** Do measurements reflect true values?
4. **Validity:** Do values fall within acceptable domains?
5. **Timeliness:** Is data current enough for the analysis?
6. **Uniqueness:** Are records properly deduplicated?

