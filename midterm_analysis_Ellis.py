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

X = sm.add_constant(df[['credit_score', 'debt_to_income']]) # Assigns the credit score and debt to income variables in the dataframe to be the X, or predictors 
y = df['approved'] # Assigns the dependent variable to be approved, this is a binary value either 0 for denied or 1 for approved

model_OLS = sm.OLS(y, X).fit() # using a OLS model with the variables we defined above
print(model_OLS.summary()) # Printing model summary

# ── Problem 2: Logistic Regression ───────────────────────────────────────────
# Run a logistic regression with the same predictors and outcome variable.
# Print the full model summary.

model_Log = sm.Logit(y, X).fit() # Uses the same variables we defined previously, this time using a Logistic Regression Model using sm.Logit function
# The predictor X variables already have the constant added from above, and the dependent y variable is binary
print(model_Log.summary()) # Printing model summary


# ── Problem 3: OLS Fitted Values ──────────────────────────────────────────────
# Print the fitted values from your OLS model.
# Count and print how many predictions fall outside the range [0, 1].

OLS_fitted_values = model_OLS.fittedvalues # statsmodels has an object for fitted values, here we are defining a variable to access and work with them easier
print("\nThe OLS Fitted Values are:")
print(OLS_fitted_values) # prints the variable we defined for fitted values of the OLS model

outside_range = OLS_fitted_values[(OLS_fitted_values < 0) | (OLS_fitted_values > 1)] # outside_range will be variable that stores data from OLS fitted values that pass 
# test being either less than 0 or greater than 1. It will be a subset of data from fitted values
print("\nValues that are outside of the range [0,1]:") 
print(outside_range) # Showing the values which are outside the range, can examine to see how the model is performing or making errors
print("\nCount of how many predictions fall outside of the range [0,1]:")
print(len(outside_range)) # The length of this subset of data will show how many fitted values fall outside the range, we are just printing the count result


# ── Problems 4 & 5: Written Answers ──────────────────────────────────────────
# Answer Problems 4 and 5 in your Word document (submitted via Blackboard).
# No additional code is required here.
