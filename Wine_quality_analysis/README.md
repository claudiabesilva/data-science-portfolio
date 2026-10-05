# Wine Quality: Statistical Analysis of Physicochemical Properties

Statistical analysis of ~6,500 Portuguese *vinho verde* wines (red and white) to identify which physicochemical properties are associated with sensory quality scores.

## Question

Which physicochemical measurements are associated with higher quality scores, and how well can a simple model separate good wines (score of 7 or above) from the rest?

## Data

- **Source:** [UCI Machine Learning Repository, Wine Quality](https://archive.ics.uci.edu/dataset/186/wine+quality)
- **Size:** 6,497 samples (1,599 red and 4,898 white; confirm the counts and any changes after cleaning in the notebook), 11 physicochemical variables, one sensory quality score (0 to 10)
- **License:** CC BY 4.0
- **Citation:** Cortez, P., Cerdeira, A., Almeida, F., Matos, T., & Reis, J. (2009). Wine Quality [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C56S3T

## Methods

- Data quality checks (missing values, duplicates, class balance)
- Exploratory analysis: distributions, correlations, quality by wine color
- Hypothesis testing: Welch t-test and Mann-Whitney U (red vs white alcohol), one-way ANOVA with Tukey HSD and Kruskal-Wallis (alcohol by quality group), effect sizes
- Linear regression (OLS) with standardised coefficients, VIF, residual diagnostics and Breusch-Pagan test
- Logistic regression for "good wine": odds ratios with confidence intervals (statsmodels) and held-out evaluation with precision, recall and ROC AUC (scikit-learn)

## Key findings

> Replace with your own results after running the notebook. Keep each finding to one sentence with a number.

1. *(Example format)* Alcohol shows the strongest positive association with quality (standardised coefficient of X).
2. *(Example format)* The logistic model reaches a ROC AUC of X on held-out data, with recall of X for good wines.
3. *(Example format)* Red and white wines differ in alcohol by X percentage points (Cohen's d of X).

## Limitations

- Quality is a subjective, ordinal sensory score rather than a direct measurement
- Classes are imbalanced, with few excellent and few poor wines
- Results describe associations, not causal effects
- The data covers only *vinho verde* wines from one region
- Some predictors are correlated with each other (see the VIF table in the notebook)

## How to run

```bash
pip install pandas numpy matplotlib seaborn scipy statsmodels scikit-learn ucimlrepo jupyter
jupyter notebook wine_quality_analysis.ipynb
```

The dataset is downloaded automatically through the `ucimlrepo` package (id 186), so no manual download is needed.

## Tools

`pandas` `numpy` `matplotlib` `seaborn` `scipy` `statsmodels` `scikit-learn`
