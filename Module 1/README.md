# Module 1 The Nature of Data

## What is Data & Why it matters?

- Data represents **recorded observations** or **measurements** of phenomena in the world, systematically captured to enable analysis, inference, and decision-making.
- Why data matters:
	- Evidence-Based decision Making
	- Predictive Power
	- Scientific Discovery
	- Business Intelligence
$$
  \text{Reality} \xrightarrow{\text{Measurement}} \text{Raw Data} \xrightarrow{\text{Structuring}} \text{Organized Data} \xrightarrow{\text{Analysis}} \text{Information} \xrightarrow{\text{Context}} \text{Knowledge}
$$
---
## Types of Data

### 1. Numeric Data (Quantitative)

#### A. Continuous Data
Data that can take any value within an interval on the real number line $\mathbb{R}$ 
$$
X \epsilon [a,b] \subset \mathbb{R}, \hspace{2cm} where |[a, b]| = \infty
$$

#### B. Discrete Data
Data that can take only specific, countable values, typically integers representing counts.
$$
X \epsilon Z \hspace{1cm} X \epsilon \{x_1, x_2, ..., x_n\} \hspace{1cm} where n < \infty \text{ or countably infinite} 
$$
### 2. Categorical Data (Qualitative)

#### A. Nominal Data
Categories with no inherent order or ranking - they are merely labels.
$$
X \epsilon C = \{c_1, c_2, ..., c_k\} \text{ where no ordering } c_i < c_j \text{ exists}
$$

#### B. Ordinal Data
Categorical data with a meaningful order or ranking, but intervals between categories are not necessarily equal.
$$
X \epsilon O = \{o_1, o_2, ..., o_k\}, \text{ where } o_1<o_2<...<o_k
$$

#### C. Binary Data
Categorical data with exactly two categories, often representing presence/absence, yes/no, true/false. 
$$
X \epsilon \{0,1\} \hspace{1cm} or \hspace{1cm} X \epsilon \{False, True\}
$$

---

## The Philosophy of Measurement: What does it mean to Measure Something?

Stevens' Four Levels of Measurements (1946):
1. Nominal: Classification only.
2. Ordinal: Ordering/ranking.
3. Interval: Ordered with equal intervals (but no true zero)
4. Ratio: Ordered with equal intervals AND a true zero.

Representational Theory of Measurement: Measurement creates an isomorphism (structure-preserving mapping) between:
- Empirical relations (observed in reality)
- Numerical relations (in abstract mathematics)

**Validity, Reliability and Precision**
- Validity: Does the measurement capture what it intends to measure?
	- _Example_: Does IQ truly measure intelligence or something narrower?
- Reliability: Do repeated measurements yield consistent results?
	- _Example_: Low variance in measurement error $\epsilon$
- Precision: How fine-grained is the measurement?
	- Related to the number of significant digits or decimal places.

---

## Data Structures: Why Rectangular Data?

Rectangular Data - organized as rows (observations/records) and columns (variables/features).

Why this structure?
1. **Mathematical Tractability:** Matrix operations enable efficient computation.
2. **Statistical Theory:** Most methods (regression, ANOVA, PCA) assume rectangular input.
3. **Software Optimization:** Data frames/matrices have optimized memory layout and indexing.
4. **Interpretability:** Rows-as-observations, columns-as-features is intutive.
5. **Cross-sectional Analysis:** Each row is independent, enabling IID (independent and identically distributed) assumptions.

Key Terminologies:
1. **Records/Observations/Rows:** Individual cases in the dataset.
2. **Features/Variables/Columns:** Measured attributes.
3. **Outcome/Response/Target:** Variable to predict (if supervised learning)
4. **Predictors/Inputs:** Variables used for prediction.

---

## Unstructured vs Structured Data

| Aspect           | Structured Data                      | Unstructured Data                  |
| ---------------- | ------------------------------------ | ---------------------------------- |
| **Format**       | Tables, rows, columns                | Text, images, video, audio         |
| **Schema**       | Predefined, rigid                    | Flexible or absent                 |
| **Storage**      | Relational Databases                 | Data lakes, NoSQL, file systems    |
| **Queryability** | SQL, direct queries                  | Requires processing (NLP, CV)      |
| **Analysis**     | Statistical methods, ML              | Deep learning, specialized methods |
| **Examples**     | Transaction records, sensor readings | Social media posts, medical images |

ETL (Extract Transform Load):
$$
\text{Unstructured} \xrightarrow{\text{Feature Extraction}} \text{Structured} \xrightarrow{\text{Analysis}} \text{Insights}
$$

---

## How Data Type Influences Analysis Choice?

The data type fundamentally determines which statistical methods, visualizations, and models are appropriate.

**Decision Tree for Analysis:**
```text
Data Type
├── Numeric
│   ├── Continuous
│   │   ├── Visualization: Histogram, Density plot, Boxplot
│   │   ├── Summary: Mean, SD, Median, IQR
│   │   └── Models: Linear regression, t-tests, ANOVA
│   └── Discrete
│       ├── Visualization: Bar chart, Count plot
│       ├── Summary: Count, Mode, Frequency
│       └── Models: Poisson regression, Count models
└── Categorical
    ├── Nominal
    │   ├── Visualization: Bar chart, Pie chart
    │   ├── Summary: Mode, Proportions
    │   ├── Encoding: One-hot encoding
    │   └── Tests: Chi-square test
    └── Ordinal
        ├── Visualization: Ordered bar chart
        ├── Summary: Median, Mode, Quantiles
        ├── Encoding: Ordinal encoding
        └── Tests: Mann-Whitney U, Kruskal-Wallis

```

### Statistical Test Selection by Data Type
Hypothesis testing depends critically on data types:

| Comparison                      | Data Types              | Appropriate Test     |
| ------------------------------- | ----------------------- | -------------------- |
| One sample vs population value  | Continuous              | One-sample t-test    |
| Two independent groups          | Continuous              | Independent t-test   |
| Two paired groups               | Continuous              | Paired t-test        |
| Three+ independent groups       | Continuous              | ANOVA                |
| Two independent groups          | Ordinal                 | Mann-Whitney U test  |
| Three+ independent groups       | Ordinal                 | Kruskal-Wallis test  |
| Two categorical variables       | Nominal x Nominal       | Chi-square test      |
| Relationship between continuous | Continuous x Continuous | Pearson correlation  |
| Relationship between ordinal    | Ordinal x Ordinal       | Spearman correlation |

---

