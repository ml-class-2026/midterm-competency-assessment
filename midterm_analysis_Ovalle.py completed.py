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

import numpy as np
print("\n" + "="*50)
print("Section 1: OLS Regression")
print("="*50)
data = pd.DataFrame({'credit_score': [689,595,745,728,761], 'debt_to_income':[0.006,0.33,0.48,0.29,0.27], 'approved':[0,0,0,0,1]})
x= data[['credit_score', 'debt_to_income']]
y= data['approved']
model =sm.ols(y,x).fit()
print(model.summary())

                                      


# ── Problem 2: Logistic Regression ───────────────────────────────────────────
# Run a logistic regression with the same predictors and outcome variable.
# Print the full model summary.
print("\n" + "="*50)
print("Section 2: Linear Regression")
print("="*50)
data = pd.DataFrame({'credit_score': [689,595,745,728,761], 'debt_to_income':[0.06,0.33,0.48,0.29,0.27],'approved':\ [0,0,0,0,1] })
x= data[['credit_score', 'debt_to_income']]
y= data['approved']
model = sm.logit(y,x)
result = model.fit()
print(result.summary())

# ── Problem 3: OLS Fitted Values ──────────────────────────────────────────────
# Print the fitted values from your OLS model.
# Count and print how many predictions fall outside the range [0, 1].

print("\n" + "="*50)
print("Section 3: Fitted Values")
print("="*50)
data = pd.DataFrame({ 'credit_score': [689,595,745,728,761], 'debt_to_income':[0.06,0.33,0.48,0.29,0.27], 'approved\': [0,0,0,0,1]})
model = sm.OLS(y,x).fit()
fitted_values = model.fittedvalues
print("Fitted values:")
print(fitted_values)
num_observations =len(fitted_values)
print("Number of observations:", num_observations)



# ── Problems 4 & 5: Written Answers ──────────────────────────────────────────
# Answer Problems 4 and 5 in your Word document (submitted via Blackboard).
# No additional code is required here.
