# Measures of Variability (dispersion)

**Measures of Location** tell us where the center of the data lies, but they provide only half the picture. To truly understand the data, we need to understand its spread - how dispersed observations are around the center. 
Variability quantifies uncertainty, heterogeneity, and risk, which are fundamental concepts in both descriptive statistics and inferential reasoning.

Understanding variability allows us to:
- Quantify uncertainty in predictions and estimates.
- Assess risk in financial, medical, and operational decisions.
- Detect anomalies by distinguishing normal variation from systematic shifts.
- Make informed comparisons across groups, treatments, or time periods.

In probability theory, variance is called the **second moment** of a distribution (the first being the mean), capturing how data scatters around its center.

---
## Range

The range is the simplest measure of variability:
$$
\text{Range} = max(x) - min(x)
$$
**Limitations:**
- Highly sensitive to outliers
- Ignores the distribution of bulk of the data
- Not useful for robust statistical inference

---
## Variance

The variance measures the average squared deviation from the mean:
$$
s^2 = \frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar x)^2
$$
**Why square the deviations?**
- **Mathematical Reasoning:**
	1. **Sum of deviations is zero**: $\sum(x_i-\bar x)$ so averaging raw deviations is uninformative.
	2. **Magnifies large deviations:** Squaring emphasizes extreme values, making variance sensitive to outliers.
	3. **Mathematical tractability:** Squared terms are differentiable and lead to elegant optimization (e.g., least squares regression).
	4. **Connection to geometry:** Variance relates to the Euclidean distance in multidimensional space. 
- **Intuitive Reasoning:**
	1. Variance quantifies how far data points are spread from the mean on average (in squared units).
	2. It underlines many statistical models (linear regression, ANOVA, hypothesis testing).

---
## Standard Deviation

The standard deviation is the square root of the variance:
$$
s = \sqrt{s^2} = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar x)^2}
$$
**Why take the square root?**
Variance has squared units (e.g., dollars squared), which are not interpretable. The standard deviation returns to the original units of the data, making it easier to understand and communicate. 

**Interpretation:**
- Roughly 68% of data in a normal distribution lies within $\pm 1$ standard deviation of the mean.
- Standard deviation is the most widely reported measure of spread in practice. 

---
## Mean Absolute Deviation (MAD)

The Mean Absolute Deviation averages the absolute deviations from the mean:
$$
\text{MAD} = \frac{1}{n}\sum_{i=1}^{n}|x_i - \bar x|
$$
**Advantages:**
- More robust than standard deviation to extreme outliers.
- Uses absolute values instead of squares, so large deviations have less influence. 

**Disadvantages:**
- Less common in practice because deviations have better mathematical properties for statistical theory. 

---
## Median Absolute Deviation (MAD)

A robust alternative is the Median Absolute Deviation from the median:
$$
\text{MAD = Median}(|x_1 - m|, |x_2-m|, ..., |x_n -  m|)
$$
where $m$ is the median.

**Key properties:**
- Insensitive to outliers.
- Often scaled by 1.4826 to match the standard deviation for normal distributions.

---
## Interquartile Range (IQR)

The Interquartile Range measures the spread of the middle 50% of the data:
$$
\text{IQR} = Q_3 - Q_1
$$
where $Q_1$ and $Q_3$ are the 25th and 75th percentiles, respectively.

**Advantages:**
- Robust - unaffected by extreme values.
- Used in boxplots to visually identify outliers

**Application:** Outliers are usually defined as values beyond $Q_1 - 1.5 \times \text{IQR}$ or $Q_3 + 1.5 \times \text{IQR}$.

---
## Coefficient of Variation

The Coefficient of Variation (CV) standardizes the standard deviation by the mean:
$$
\text{CV} = \frac{s}{\bar x} \times 100\%
$$
**When to use:**
- To compare variability across datasets with different units or scales. 
- For example, comparing the variability of stock returns (percentages) versus temperature measurements (degrees Celsius).

**Interpretation:** A higher CV indicates greater relative variability.

---
## The Concept of "Spread"

**Spread** or **dispersion** is a fundamental statistical concept. It tells us:
- **Uncertainty:** How confident are we in our estimates? Narrow spreads imply precision.
- **Heterogeneity:** Do all observations behave similarly, or is there diversity?
- **Risk:** In finance, volatility (standard deviation) measures risk. In manufacturing, variability indicates quality control.

**Standard Deviation** is optimal under normality. **IQR** and **MAD** protect against outliers. Choose the measure that aligns with the data distribution and decision context. 

---
## Degrees of Freedom

The variance formula uses $n-1$ in the denominator, not $n$:
$$
s^2 = \frac{1}{n-1}\sum_{i=1}^{n} (x_i - \bar x)^2
$$
**Why $n-1$?**
- **Bias correction:** Using $n$ produces a biased estimate of the population variance - it systematically underestimates it. Dividing by $n-1$ corrects this bias, making the sample variance an unbiased estimator. 
- **Degrees of freedom intuition:** Once you compute the sample mean $\bar x$, you've imposed a constraint on the data. If you know $n-1$ observations and the mean, the $n$th value is determined. Thus, only $n-1$ values are "free to vary".
- **Mathematical derivation:** The expected value of the sample variance is:
$$
E\left[\frac{1}{n} \sum(x_i - \bar x)^2 \right] = \frac{n-1}{n}\sigma^2
$$
Multiplying by $\frac{n}{n-1}$ yields an unbiased estimator.

**Practical relevance:**
- For large $n, n-1 \approx n$, so distinction is negligible.
- For small samples, using $n-1$ is critical to avoid underestimating variance.
- In regression, degrees of freedom adjust for the number of estimated parameters. 

---

## Summary Comparison Table

| Measure            | Formula                               | Sensitive to Outliers? | Units      | Use Case                 |
| ------------------ | ------------------------------------- | ---------------------- | ---------- | ------------------------ |
| Range              | $max - min$                           | Yes                    | Original   | Quick rough estimate     |
| Variance           | $$\frac{1}{n-1}\sum(x_i - \bar x)^2$$ | Yes                    | Squared    | Theoretical Modeling     |
| Standard Deviation | $$\sqrt{\text{Variance}}$$            | Yes                    | Original   | Most common reporting    |
| MAD (Mean)         | $\frac{1}{n}\|x_i - \bar x\|$         | Moderately             | Original   | Robust alternative       |
| MAD (Median)       | $\text{Median}(\|x_i - m\|)$          | No                     | Original   | Highly robust            |
| IQR                | $Q_3 - Q_1$                           | No                     | Original   | Outlier detection        |
| CV                 | $\frac{s}{\bar x} \times 100\%$       | Depends on $s$         | Percentage | Cross-dataset comparison |

Variability is not noise - it is information. It tells us about the structure, stability, and uncertainty inherent in data. Choosing the right measure of dispersion depends on:
- Data distribution (symmetric vs. skewed)
- Presence of outliers
- Purpose of analysis (description, inference, risk assessment)
