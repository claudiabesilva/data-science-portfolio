# Wine Quality: Statistical Analysis of Physicochemical Properties

Statistical analysis of ~6,500 Portuguese *vinho verde* wines (red and white) to identify which physicochemical properties are associated with sensory quality scores.

## Question

Which physicochemical measurements are associated with higher quality scores, and how well can a simple model separate good wines (score of 7 or above) from the rest?

## Data

- **Source:** [UCI Machine Learning Repository, Wine Quality](https://archive.ics.uci.edu/dataset/186/wine+quality)
- **Size:** 6,497 samples (1,599 red and 4,898 white); 11 physicochemical variables, one sensory quality score (0 to 10)
- **License:** CC BY 4.0
- **Citation:** Cortez, P., Cerdeira, A., Almeida, F., Matos, T., & Reis, J. (2009). Wine Quality [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C56S3T

## Methods

- Data quality checks (missing values, duplicates, class balance)
- Exploratory analysis: distributions, correlations, quality by wine color
- Hypothesis testing: Welch t-test and Mann-Whitney U (red vs white alcohol), one-way ANOVA with Tukey HSD and Kruskal-Wallis (alcohol by quality group), effect sizes
- Linear regression (OLS) with standardised coefficients, VIF, residual diagnostics and Breusch-Pagan test
- Logistic regression for "good wine": odds ratios with confidence intervals (statsmodels) and held-out evaluation with precision, recall and ROC AUC (scikit-learn)

## Key findings

- Variables most associated with quality: alcohol (positively) and volatile acidity (negatively).
- A simple model separates good wines moderately well: recall = 79%, precision = 39%, ROC AUC = 0.825.

## Limitations

- Quality is a subjective, ordinal sensory score, not a measurement.
- OLS treats quality as continuous, although it is ordinal.
- The cut-off of 7 for "good" is a choice. Another threshold would give different results. 
- Classes are imbalanced: 19% of wines are good.
- Results describe associations, not causes.
- Duplicates were removed (6,497 to 5,320 wines). 
- Correlated predictors: density was dropped (VIF 14.9).
- OLS residuals do not have constant variance (Breusch-Pagan p < 0.001), so OLS p-values and CIs may be too optimistic. 
- The OLS model includes color and the logistic model does not.
- The results come from one train/test split. Another split would give slightly different numbers.
- Data covers only *vinho verde* wines from one region.

## How to run

```bash
pip install pandas numpy matplotlib seaborn scipy statsmodels scikit-learn ucimlrepo jupyter
jupyter notebook wine_quality_analysis.ipynb
```

The dataset is downloaded automatically through the `ucimlrepo` package (id 186), so no manual download is needed.

## Tools

`pandas` `numpy` `matplotlib` `seaborn` `scipy` `statsmodels` `scikit-learn`
