# MGT 665 — Midterm Competency Assessment
**Northwood University | DeVos Graduate School | Spring 2026**
Instructor: Adam Guerrero

---

## Overview

Welcome to the Midterm Competency Assessment repository! This repo contains everything you need to complete the programming portion of the midterm. The assessment covers Chapters 1 through 7 and is built around a real business problem: predicting loan approvals at a regional bank using two different modeling approaches.

---

## What Is in This Repository

| File | What It Is | What You Do With It |
|---|---|---|
| `loan_approval.csv` | Dataset of 200 loan applicants | Load it in your Python program — do not modify it |
| `midterm_starter.py` | Starter Python program with imports and data loading | Rename it, complete the analysis, and submit it |
| `README.md` | These instructions | Read before you start |

---

## Before You Start — Activate Your Environment

As always, make sure your `islp` conda environment is activated before running your program. This is where all the packages you need (`pandas`, `statsmodels`, etc.) are installed.

**Open Anaconda Prompt and run:**
```
conda activate islp
```

You should see `(islp)` appear at the start of your prompt. If you skip this step and run from the base environment, you will likely see a `ModuleNotFoundError` for `statsmodels`.

### Running your program

**Option A — Anaconda Prompt:**
```
conda activate islp
python midterm_analysis_[YourLastName].py
```

**Option B — VS Code:**
- Open VS Code and open your cloned midterm folder
- Check the interpreter in the bottom right corner — make sure it says `islp (3.11.15)`
- If it does not, click it and select the islp environment
- Press `Ctrl+F5` to run

> Note: You do not need Jupyter Notebook for this assignment. You are writing and submitting a `.py` file, not a `.ipynb` notebook.

---

## Step-by-Step Instructions

### Step 1 — Fork and clone this repository
1. Go to `github.com/ml-class-2026/midterm-competency-assessment`
2. Click **Fork** (top right) — this creates your own personal copy
3. Open GitHub Desktop → File → Clone Repository → select your forked repo
4. Choose a local folder and click **Clone**

### Step 2 — Rename the starter file
Rename `midterm_starter.py` to `midterm_analysis_[YourLastName].py`

For example: `midterm_analysis_Guerrero.py`

### Step 3 — Complete the analysis
Open the renamed file in VS Code (with the `islp` interpreter selected) and complete Problems 1, 2, and 3. Problems 4 and 5 are written answers — complete those in your Word document.

Make sure your program runs from top to bottom without errors before submitting.

### Step 4 — Commit, push, and open a pull request
1. Open GitHub Desktop — you should see your renamed/modified `.py` file listed under Changes
2. Write a meaningful commit message, for example: `Add midterm analysis — [Your Name]`
3. Click **Commit to main**
4. Click **Push origin**
5. Go to your fork on github.com and click **Contribute → Open pull request**
6. Title your pull request: `Midterm Submission — [Your Name]`
7. Click **Create pull request**

### Step 5 — Submit your Word document via Blackboard
1. Download the Word document from Blackboard (under Week 4 → Midterm Competency Assessment)
2. Fill in your written answers directly in the document
3. Go to Blackboard → MGT 665 → Week 4 → Midterm Competency Assessment
4. Upload your completed Word document and submit

---

## Submission Checklist

- [ ] Forked the repo from `github.com/ml-class-2026/midterm-competency-assessment`
- [ ] Cloned it to your computer using GitHub Desktop
- [ ] Renamed the starter file to `midterm_analysis_[YourLastName].py`
- [ ] Completed Problems 1, 2, and 3 in Python
- [ ] Program runs from top to bottom without errors
- [ ] Committed with a meaningful message and pushed to GitHub
- [ ] Opened a pull request titled: `Midterm Submission — [Your Name]`
- [ ] Completed all written answers (Problems 4 & 5, all 20 MC questions) in the Word document
- [ ] Uploaded completed Word document to Blackboard

---

## Submission Summary

| What | Where | Format |
|---|---|---|
| Python analysis program | GitHub pull request | `.py` file |
| Written answers (Problems 4 & 5 + all MC) | Blackboard | Word document (`.docx`) |

---

## Questions?

Post in the **Ask the Instructor** forum on Blackboard or email me directly. I respond within 24 hours. You can also join me on **Fridays at 5 PM** for live office hours.

Good luck — you've got this! 💪
