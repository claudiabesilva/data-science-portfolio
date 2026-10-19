# Wine Quality Analysis: project context

## About me
Claudia, Chemical Engineer (PhD), based in the Netherlands. Building a data analysis / data science portfolio on GitHub:
https://github.com/claudiabesilva/data-science-portfolio

This project will live in its own folder inside that repository (`Wine_Quality_Analysis/`), like the existing projects.

## Goal of this project
Add statistics and predictive modelling to a portfolio that so far contains only exploratory analysis.

Question: which physicochemical properties are associated with sensory quality scores, and how well can a simple model separate good wines (quality of 7 or above) from the rest?

## Data
- UCI Wine Quality, id 186, loaded with `ucimlrepo` (`fetch_ucirepo(id=186)`, use `.data.original`)
- 6,497 samples (1,599 red, 4,898 white), 11 physicochemical features, quality score, color
- License CC BY 4.0. Citation: Cortez, P., Cerdeira, A., Almeida, F., Matos, T., & Reis, J. (2009). Wine Quality [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C56S3T

## Files
- `wine_quality_analysis.ipynb`: notebook skeleton. Code is written but has NEVER been run. Expect small fixes (column names, color labels, library versions).
- `README.md`: template. "Key findings" are placeholders.

## Planned steps
1. Data quality checks (missing values, duplicates, class balance)
2. EDA (distributions, correlations, quality by color)
3. Hypothesis tests: Welch t-test and Mann-Whitney (red vs white alcohol), ANOVA + Tukey HSD + Kruskal-Wallis (alcohol by quality group), effect sizes
4. OLS regression with standardised coefficients, VIF, residual diagnostics, Breusch-Pagan
5. Logistic regression: odds ratios with CIs (statsmodels) and held-out evaluation (precision, recall, ROC AUC)
6. Conclusions and limitations

## How I want to work
- I am learning. Explain what each step does and why, briefly, before or after running it.
- Run cells one section at a time and show me the results before moving on.
- Do NOT write the interpretations, conclusions or "Key findings" for me. Those cells are mine. You can review what I write and point out errors or overclaims.
- Never invent results or numbers. Every number in the README must come from an actual run.
- Keep the analysis honest: report effect sizes, not only p-values; state limitations clearly.
- When there is a decision (for example, dropping duplicates, handling collinearity), explain the options and let me choose.

## Writing style for README and markdown cells
- English, professional and direct
- No em dashes, no marketing language, no "passionate about", no "transitioning"
- Short sentences, one finding per line, each with a number

## Later projects (separate folders, separate sessions)
2. Combined Cycle Power Plant (UCI id 294): regression, scikit-learn
3. Steel Industry Energy Consumption (UCI id 851): energy, feature engineering
4. Netherlands energy forecasting (ENTSO-E): time series
5. Tennessee Eastman Process (Harvard Dataverse): fault detection
6. Power BI dashboard based on project 3 or 4
