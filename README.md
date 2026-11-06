# Customer Churn Prediction

## Project Overview

Customer Churn Prediction is a Machine Learning project that aims to identify customers who are likely to discontinue a company's services.

The project uses customer information, subscription details and service usage patterns to train classification models and predict whether a customer will churn.

The primary objective is to help businesses identify potential customer loss and make better customer retention decisions.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook

## Dataset

The dataset contains customer information, including:

- CustomerID
- Age
- Gender
- Tenure
- MonthlyCharges
- ContractType
- InternetService
- TotalCharges
- TechSupport
- Churn

**Target Variable:** Churn

- 0 – No Churn
- 1 – Churn

## Project Workflow

1. **Data Loading and Exploration**
   - Loaded the dataset using Pandas.
   - Inspected dataset structure and statistical information.
   - Identified missing values and duplicate records.
   - Examined unique categorical values and invalid numerical values.

2. **Data Preprocessing**
   - Handled missing InternetService values.
   - Separated input features (X) and target (y).
   - Applied One-Hot Encoding to categorical features.
   - Converted churn labels into numerical values.
   - Split the dataset into training and testing sets.
   - Applied StandardScaler for Logistic Regression.

3. **Model Training**
   - Logistic Regression
   - Random Forest Classifier

4. **Model Evaluation**
   - Accuracy
   - Confusion Matrix
   - Precision
   - Recall
   - F1-Score
   - ROC-AUC Score
   - ROC Curve

## Model Performance

Results from the current 80:20 train-test split:

| Evaluation Metric | Logistic Regression | Random Forest |
|---|---:|---:|
| Accuracy | 97% | 100% |
| Precision (Churn) | 96.7% | 100% |
| Recall (Churn) | 100% | 100% |
| F1-Score (Churn) | 98% | 100% |
| ROC-AUC | 99.53% | 100% |

Random Forest achieved the best performance on the current test dataset.

*Note: These results are based on a single train-test split and do not guarantee equivalent real-world performance.*

## Project Structure

```text
Customer-Churn-Prediction/
│
├── archive/
│   └── customer_churn_data.csv
│
├── customer_churn_preprocessing.ipynb
│
└── README.md
```

## How to Run

1. Clone the repository:

   ```bash
   git clone <your-repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd Customer-Churn-Prediction
   ```

3. Install the required libraries:

   ```bash
   pip install pandas numpy matplotlib scikit-learn jupyter
   ```

4. Launch Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

5. Open `customer_churn_preprocessing.ipynb` and execute the cells sequentially.

## Conclusion

This project demonstrates the application of Machine Learning classification techniques to customer churn prediction.

By comparing Logistic Regression and Random Forest, the project explores how different algorithms learn customer behaviour patterns and how classification evaluation metrics help assess their performance.
