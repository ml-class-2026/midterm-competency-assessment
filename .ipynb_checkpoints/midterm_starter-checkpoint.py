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

# YOUR CODE HERE


# ── Problem 2: Logistic Regression ───────────────────────────────────────────
# Run a logistic regression with the same predictors and outcome variable.
# Print the full model summary.

# YOUR CODE HERE


# ── Problem 3: OLS Fitted Values ──────────────────────────────────────────────
# Print the fitted values from your OLS model.
# Count and print how many predictions fall outside the range [0, 1].

# YOUR CODE HERE


# ── Problems 4 & 5: Written Answers ──────────────────────────────────────────
# Answer Problems 4 and 5 in your Word document (submitted via Blackboard).
# No additional code is required here.
