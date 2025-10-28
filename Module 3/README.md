# Measures of Location (Central Tendency)

Measures of location, also called measures of central tendency, describe where the data "centers" - the typical or representative value around which observations cluster. 
Understanding them is fundamental to both descriptive and inferential statistics, as they provide a concise summary of the distribution's location or average tendency.

---
## Mean

The mean (or arithmetic mean) of a dataset $x_1, x_2, x_3, ...,x_n$ is defined as:
$$
\bar x = \frac{1}{n} \sum^n_{i=1}x_i
$$
It is the point where the sum of deviations equals zero. It captures the _expected value_ under the assumption that all data points are equally reliable and the distribution is symmetric.

**When to use:**
- Appropriate for symmetric distributions without outliers
- Used in regression, variance analysis, and most parametric inference methods because its mathematical tractability.
- Reflects total magnitude well.

> It is sensitive to outliers because each observation contributes equally to the sum.

---
## Median

The median is the middle of the sorted data. Formally,
$$
\text{Median}(x) = 
\begin{cases}
x_{n+1}/2, &\text{if $n$ is odd} \\
\frac{x_{(n/2)} + x_{(n/2 + 1)}}{2}, &\text{if $n$ is even}
\end{cases}
$$
Unlike the mean, the median only depends on the rank order, not on the magnitude of extreme values.

**Why we need it:**
- When the distribution is skewed or contains outliers, the median better represents the 
  "typical" observation
- It is a robust estimator of location, unaffected by data errors or extreme values.

---
## Mode

The mode is the most frequent value in the dataset:
$$
\text{Mode} = \text{arg}\max_x f(x)
$$
This measure is crucial for categorical data where mean and median are undefined.
For continuous data, the mode may correspond to the peak of the density function - indicating the most probable value.

**When it's useful:**
- Nominal (categorical) data
- Multimodal distributions - revealing multiple clusters or subpopulations.

---
## Trimmed Mean

Removes a specific percentage of the smallest and largest observations before calculating the mean:
$$
\bar x_{trimmed} = \frac{1}{n-2k}\sum_{i=k+1}^{n-k}x_{(i)}
$$
where $k$ values are trimmed from each end.

**Why use it:**
- Provides a compromise between the mean and median.
- Reduces sensitivity to outliers while retaining more data than the median

---
## Weighted Mean

The weighted mean generalizes the mean by assigning weights $w_i$ to each observation:
$$
\bar x_w = \frac{\sum_{i=1}^{n}w_ix_i}{\sum_{i=1}^nw_i}
$$
**When to use:**
- Some observations represent more individuals (e.g., state population-weighted averages).
- Measurement precision differs (e.g., sensor data with varying reliability).
- In survey analysis, to adjust for sampling bias.

---
## Why These Measures Differs

| Measure       | Sensitive to Outliers? | Applicable Data Types    | Interpretation                            |
| ------------- | ---------------------- | ------------------------ | ----------------------------------------- |
| Mean          | Yes                    | Numeric (Interval/Ratio) | Balancing point of data                   |
| Median        | No                     | Numerica/Ordinal         | Middle position                           |
| Mode          | No                     | Nominal/Ordinal          | Most common observation                   |
| Trimmed Mean  | Moderately             | Numeric                  | Robust compromise between mean and median |
| Weighted Mean | Depends on weights     | Numeric                  | Adjusted average reflecting importance    |

Differences reflect underlying asymmetry, heterogeneity and measurement design.

---
## Choosing the Right Measure

**Decision Framework:**
- If data are symmetric and complete: use the **mean**
- If data are skewed or contain outliers: prefer **median** or **trimmed mean**
- If data are categorical: use the **mode**
- If observations have varying relevance or reliability: use the **weighted mean**
- For every robust estimation in small samples: median or trimmed mean provide better inference stability.

**Visualization Tip:**
Inspect histogram or boxplots before selection. Measures of central tendency are most informative when interpreted alongside measures of spread (variance, IQR, MAD).

---
## Deeper Mathematical Insight

From a probabilistic viewpoint:
- The **mean** minimizes the **sum of squared deviations (SSD)**
$$
\bar x = arg \min_{\mu} \sum(x_i-\mu)^2
$$
- Them **median** minimizes the **the sum of absolute deviations (SAD)**
$$
\bar x = arg \min_{\mu}\sum |x_i-\mu|
$$
Thus, the mean optimizes efficiency under normality, while the median optimizes robustness under deviations from normality - revealing their complementary strengths.