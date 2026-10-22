# Wine Quality: Statistical Analysis of Physicochemical Properties

Statistical analysis of ~6,500 Portuguese *vinho verde* wines (red and white) to identify which physicochemical properties are associated with sensory quality scores.

## Question

Which physicochemical measurements are associated with higher quality scores, and how well can a simple model separate good wines (score of 7 or above) from the rest?

## Data

- **Source:** [UCI Machine Learning Repository, Wine Quality](https://archive.ics.uci.edu/dataset/186/wine+quality)
- **Size:** 6,497 samples (1,599 red and 4,898 white); 5,320 wines after removing 1,177 duplicates; 11 physicochemical variables, one sensory quality score (0 to 10)
- **License:** CC BY 4.0
- **Citation:** Cortez, P., Cerdeira, A., Almeida, F., Matos, T., & Reis, J. (2009). Wine Quality [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C56S3T

## Methods

- Data quality checks (missing values, duplicates, class balance)
- Exploratory analysis: distributions, correlations, quality by wine color
- Hypothesis testing: Welch t-test and Mann-Whitney U (red vs white alcohol), one-way ANOVA with Tukey HSD and Kruskal-Wallis (alcohol by quality group), effect sizes
- Linear regression (OLS) with standardised coefficients, VIF, residual diagnostics and Breusch-Pagan test
- Logistic regression for "good wine": odds ratios with confidence intervals (statsmodels) and held-out evaluation with precision, recall and ROC AUC (scikit-learn)

## Analysis decisions

- **Duplicates removed (6,497 to 5,320 wines):** 1,177 rows were exact copies. Keeping them would count the same wine more than once, and copies could land in both the training and test sets.
- **Density dropped:** VIF = 14.9 and correlation with alcohol = -0.67. Removing it lowered the condition number from 284,775 to 5,116 and changed R² from 0.311 to 0.306.
- **Color in OLS, not in logistic regression:** the logistic model uses only the 10 physicochemical measurements, so its odds ratios describe the chemistry and not wine type.

## Key findings

- Alcohol is the variable most associated with quality (positively): +0.40 quality points per SD in OLS, odds ratio 3.11 (95% CI 2.77 to 3.50) per SD for a good wine.
- Volatile acidity is the strongest negative variable: -0.24 quality points per SD in OLS, odds ratio 0.54 (95% CI 0.46 to 0.63) per SD for a good wine.
- Red vs white alcohol: difference of -0.16 % vol (red lower), Cohen's d = -0.13, Welch t-test p < 0.001.
- Alcohol by quality group: ANOVA F = 896.2, eta-squared = 0.25; Tukey HSD shows high-quality wines at +1.66 % vol vs low-quality (95% CI 1.57 to 1.75); Kruskal-Wallis p < 0.001 agrees.
- Logistic model on the held-out test set (1,330 wines, 19% good): recall = 79% (200 of 252 good wines found), precision = 39% (about twice the 19% base rate), ROC AUC = 0.825.
- With `class_weight="balanced"`, recall is higher and precision lower: 309 of the 509 wines flagged as good (about 6 in 10) are not good.

## Limitations

- Quality is a subjective, ordinal sensory score, not a measurement.
- OLS treats quality as continuous, although it is ordinal.
- The cut-off of 7 for "good" is a choice. Another threshold would give different results. 
- Classes are imbalanced: 19% of wines are good.
- Results describe associations, not causes.
- OLS residuals do not have constant variance (Breusch-Pagan p < 0.001), so OLS p-values and CIs may be too optimistic. 
- Fixed acidity may reflect wine color, which the logistic model does not include.
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
