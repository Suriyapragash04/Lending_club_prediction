# Lending Club Loan Defaulter Prediction
![th](https://github.com/Suriyapragash04/Lending_club_prediction/assets/105835042/0e07c110-b14d-45c5-91cc-2ce42b999e38)

## Introduction

LendingClub, headquartered in San Francisco, California, is a leading peer-to-peer lending company. It holds the distinction of being the first peer-to-peer lender to register its offerings as securities with the Securities and Exchange Commission (SEC) and to facilitate loan trading on a secondary market. LendingClub stands as the world's largest peer-to-peer lending platform.

## Objective

Our primary objective is to determine "Who can repay their loans?" To achieve this, we delve into several subsidiary questions:

- Who qualifies for loans?
- What types of loans are being issued?
- How reliable is LendingClub's loan grading system?
- What are the critical data points for predicting loan repayment?

We address these questions and embark on building precise machine learning algorithms to answer our core question.

## About the Data

The dataset utilized in this project was sourced from the LendingClub website. It encompasses comprehensive loan data spanning from 2007 to 2021, including the current loan status and the most recent payment information. This dataset consists of approximately 3,000,000 observations and 141 features. For our analysis, we focus on the data from the last four years, extracting features relevant to borrowers and saving them in a CSV file.

## Exploratory Data Analysis (EDA)
![th](https://github.com/Suriyapragash04/Lending_club_prediction/assets/105835042/08112b52-c10a-4cfd-bd6e-34124a3e3e39)

Exploratory Data Analysis (EDA) is a pivotal step in any Data Analysis or Data Science endeavor. EDA entails a systematic exploration of the dataset to uncover patterns, anomalies (outliers), and to formulate hypotheses based on our understanding of the data. Key aspects of our EDA process include:

- Generating summary statistics for numerical data.
- Creating diverse graphical representations for a comprehensive understanding.
- Addressing missing values within the dataset.
- Detecting and managing outliers using the Z-score method.
- Establishing correlations within the data.

Further details on these EDA steps can be found in our project report.

## Model Building

In this project, we deploy the following models to predict loan status:

- Logistic Regression
- Random Forest Classifier
- XGBoost Classifier
- KNN Classifier

## Model Evaluation

Comparing these models, we find that the Random Forest model exhibits the highest accuracy at 78 percent for test data. Extensive metrics comparisons reinforce our decision to choose Random Forest for model deployment.

## Deployment

### Creating the Web Application with Flask
To create the web application, we chose Flask, a lightweight web framework for Python. Flask allowed us to build a simple and efficient web interface for our model. We designed a user-friendly interface that accepts input data, such as borrower information, and passes it to the model for prediction.

### Setting Up a Heroku Account
To deploy our web application, we needed a Heroku account. Heroku offers a free tier that is suitable for small-scale projects and testing. We signed up for an account and installed the Heroku Command Line Interface (CLI) to facilitate deployment.

### Creating a Heroku App
Using the Heroku CLI, we created a new Heroku app. This app served as the container for our web application. Heroku automatically provided us with a web URL where our app would be accessible once deployed.

In summary, deploying our loan defaulter prediction model on Heroku using Flask was a pivotal step in making our machine learning solution accessible to users. It enabled stakeholders to interact with the model through a user-friendly web interface, making it a valuable tool for decision-making in the lending domain. The deployment process, from model preparation to continuous integration and scaling, ensured the reliability and availability of our application to meet user demands.

![image](https://github.com/Suriyapragash04/Lending_club_prediction/assets/105835042/2239ffa6-7b20-48ff-9757-11ba3a571efc)

## Conclusion

During our EDA, we uncovered specific risk categories. For high-risk borrowers, a thorough analysis of their profiles is imperative, enabling informed decisions based on their credit history. Notable findings include:

1. Loans with higher interest rates tend to have more defaulters. Applicants with high-interest rates should undergo rigorous background checks.
2. Debt consolidation purposes often correlate with a higher likelihood of default. Such applicants should be scrutinized carefully.

Our preference for tree-based models stems from their superior accuracy. When LendingClub utilizes these models, our aim is to assign each loan a probability, empowering LendingClub to make informed decisions rather than simply accepting or denying loans.

*Please feel free to explore the project code and detailed insights in the project repository.*
