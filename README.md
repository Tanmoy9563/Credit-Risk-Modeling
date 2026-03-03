💳 Credit Risk Modeling using Machine Learning

📌 Project Overview

This project builds a Credit Risk Prediction Model to classify whether a loan applicant is likely to default (1) or not default (0). The objective is to assist financial institutions in minimizing financial losses by improving risk assessment using Machine Learning techniques.

The final selected model is XGBoost Classifier, chosen after comparing multiple ensemble models.

🎯 Business Objective

Predict loan default probability

Reduce credit risk exposure

Support data-driven loan approval decisions

Improve overall portfolio quality

📂 Project Workflow

1️⃣ Data Collection

The dataset consists of structured financial and demographic information of loan applicants, including:

Age

Sex

Housing

Employment details

Loan amount

Credit history

Duration

Target variable (Default: 0/1)

2️⃣ Data Preprocessing

Handling missing values

Removing duplicates

Encoding categorical variables (Label / One-Hot Encoding)

Outlier treatment

Train-Test split (80-20)

Handling class imbalance (class weights / resampling if required)

3️⃣ Exploratory Data Analysis (EDA)

Target variable distribution

Correlation analysis

Feature relationships with default

Default rate across income and loan segments

Class imbalance check

Libraries used: Pandas, NumPy, Matplotlib, Seaborn

4️⃣ Feature Engineering

Creation of derived financial indicators

Binning continuous variables where required

Removing highly correlated features

Feature importance analysis

Optimization of input variables for better model performance

🤖 Models Implemented

Random Forest Classifier

Extra Trees Classifier

XGBoost Classifier

All models were evaluated using the same train-test split and performance metrics.

📊 Model Evaluation Metrics

Accuracy

Precision

Recall

F1 Score

ROC-AUC Score

Confusion Matrix

ROC Curve

🔎 Final Model Performance (XGBoost)

Accuracy: 0.6857

Precision: 0.7166

Recall: 0.7288

F1 Score: 0.7226

ROC-AUC: 0.7089

Confusion Matrix:

[[29 17]
 [16 43]]

ROC-AUC ≈ 0.71, indicating moderate classification performance and better discrimination ability than random guessing (0.5).

🏆 Final Model Selection

XGBoost Classifier was selected because:

Higher ROC-AUC compared to other models

Better Recall (critical in credit risk to detect defaulters)

Strong generalization performance

Robust handling of structured/tabular data

🛠️ Tech Stack

Python

Pandas

NumPy

Scikit-learn

XGBoost

Matplotlib

Seaborn


ROC-Curve:

<img width="549" height="393" alt="image" src="https://github.com/user-attachments/assets/fc11b4e1-4fab-4842-a253-e8229d492bd4" />

Example Screenshot

<img width="1126" height="736" alt="image" src="https://github.com/user-attachments/assets/27567147-f932-47de-a954-e56ccfe5a774" />


