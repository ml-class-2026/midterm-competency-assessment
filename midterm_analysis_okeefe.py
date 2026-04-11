# midterm_analysis.py
# MGT 665 — Midterm Competency Assessment
# Northwood University | DeVos Graduate School | Spring 2026
# Instructor: Adam Guerrero
#
# Instructions:
#   - Rename this file: midterm_analysis_[YourLastName].py
#   - Complete the analysis for Problems 1 through 5
#   - Run the full program before submitting to make sure it executes without errors
#   - Submit via GitHub pull request AND upload your Word document to Blackboard

# ── Imports ───────────────────────────────────────────────────────────────────
import pandas as pd
import statsmodels.api as sm

# ── Load the dataset ──────────────────────────────────────────────────────────
df = pd.read_csv('loan_approval.csv')

print("Dataset shape:", df.shape)
print("\nFirst five rows:")
print(df.head())
print("\nDescriptive statistics:")
print(df.describe())

# ── Problem 1: OLS Regression ─────────────────────────────────────────────────
# Run a linear regression (OLS) with 'approved' as the dependent variable
# and 'credit_score' and 'debt_to_income' as predictors.
# Print the full model summary.

import pandas as pd
import statsmodels.api as sm

# Load dataset
df = pd.read_csv('loan_approval.csv')

# Define predictors (X) and outcome (y)
X = df[['credit_score', 'debt_to_income']]
y = df['approved']

# Add a constant (intercept) to the predictors
X_ols = sm.add_constant(X)

# Fit the OLS model
ols_model = sm.OLS(y, X_ols).fit()

# Print the summary
print(ols_model.summary())


# ── Problem 2: Logistic Regression ───────────────────────────────────────────
# Run a logistic regression with the same predictors and outcome variable.
# Print the full model summary.

# Fit the Logistic model
logit_model = sm.Logit(y, X_ols).fit()

# Print the summary
print(logit_model.summary())


# ── Problem 3: OLS Fitted Values ──────────────────────────────────────────────
# Print the fitted values from your OLS model.
# Count and print how many predictions fall outside the range [0, 1].

# Get predicted probabilities from OLS
ols_fitted = ols_model.fittedvalues

# Count values outside [0, 1]
out_of_bounds = ols_fitted[(ols_fitted < 0) | (ols_fitted > 1)]
print(f"Number of OLS predictions outside [0, 1]: {len(out_of_bounds)}")


# ── Problems 4 & 5: Written Answers ──────────────────────────────────────────
# Answer Problems 4 and 5 in your Word document (submitted via Blackboard).
# No additional code is required here.
