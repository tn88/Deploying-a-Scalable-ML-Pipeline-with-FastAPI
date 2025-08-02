# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This is a binary classification modeltrained on the US Census Income dataset. 
It uses features such as education,workclass, occupation, and other demographic attributrs to predict whether a person earns ove $50K per year.
The model use a RandomForestClassifier from scikit-learn. The dataprocessing includes one-hot encoding for categorical features and label binaryzation for the target.

## Intended Use
The model is intended to for educational and demonstration purposes only.
It is designed to show how to build, evualate, and serve a machine learning model using a standarized pipeline.
It is not intended for deployment in real world decision-making scenarios.

## Training Data
The model was trained using the "census.csv" file provided in the project.
The dataset includes demographic information such as age, education level, marital status, race, sex, and native country.
The target label indicates whether an individual's income is over $50K.

## Evaluation Data
A portion of the dataset was set aside as a test set using a train-test split. The same preprocessing steps applied to the training data were also applied to the test data to ensure consistency.

## Metrics
The model was evaluated using precision, recall, and F1 score.
- Overall performance on test data:
Precision: 0.7419 | Recall: 0.6384 | F1: 0.6863

## Ethical Considerations
This model may inherit biases from the dataset, which contains real-world income data that can reflect inequalities.
Users should be cautious when interpreting or deploying the model's predictions, especially in scenarios that could impact individual's life.

## Caveats and Recommendations
This model is not production-ready.
It should not be used for any real hiring or financial decisions.
Performance may vary across difference subgroups; further fairness evaluation is recommended.
