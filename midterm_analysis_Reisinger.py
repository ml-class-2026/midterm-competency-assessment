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
# Prepare data for OLS
X = df[['credit_score', 'debt_to_income']]
X = sm.add_constant(X)
y = df['approved']

# Fit OLS model
ols_model = sm.OLS(y, X).fit()

print("\n--- Problem 1: OLS Regression Summary ---")
print(ols_model.summary())


# ── Problem 2: Logistic Regression ───────────────────────────────────────────
# Run a logistic regression with the same predictors and outcome variable.
# Print the full model summary.

# Prepare data for logistic regression (reuse X and y from above)
logit_model = sm.Logit(y, X).fit(disp=False)

print("\n--- Problem 2: Logistic Regression Summary ---")
print(logit_model.summary())


# ── Problem 3: OLS Fitted Values ──────────────────────────────────────────────
# Print the fitted values from your OLS model.
# Count and print how many predictions fall outside the range [0, 1].

# Fitted values from OLS
fitted_vals = ols_model.fittedvalues

print("\n--- Problem 3: OLS Fitted Values ---")
print(fitted_vals.head())

# Count predictions outside [0,1]
outside_count = ((fitted_vals < 0) | (fitted_vals > 1)).sum()
print(f"Number of OLS predictions outside [0,1]: {outside_count}")


# ── Problems 4 & 5: Written Answers ──────────────────────────────────────────
# Answer Problems 4 and 5 in your Word document (submitted via Blackboard).
# No additional code is required here.
