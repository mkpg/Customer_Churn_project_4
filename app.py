import pandas as pd
import numpy as np

df = pd.read_csv('./archive/customer_churn_data.csv')
pd.set_option('display.max_rows', None)
# print(df.describe())
# print(df[df["InternetService"].isna()])
# print(df.isna().sum())
print(df.info())
# print(df[df['Churn'] =='No'])
# print(df[df["TechSupport"] == 'No'])

no_duplicates = df[df.duplicated()]
gender_unique = df['Gender'].unique()
contract_unique = df['ContractType'].unique()
internet_service_unique = df['InternetService'].unique()
tech_support_unique = df['TechSupport'].unique()
churn_unique = df['Churn'].unique()

# ________________________________________________________________________________________

id_unique = df['CustomerID'].unique()
id_neg =df[df['CustomerID']<0]
age_neg = df[df['Age']<0]
Tenure_neg = df[df['Tenure']<0]
monthly_charges_neg = df[df['MonthlyCharges']<0]
total_charges_neg = df[df['TotalCharges']<0]
tenure_Grouped = df.groupby('TechSupport')['Churn'].value_counts()


Contract_grouped_churn = df.groupby('ContractType')['Churn'].value_counts()
tenure_grouped_churn = df.groupby('Tenure')['Churn'].value_counts()
bin_edges = [0,12,24,36,48,df['Tenure'].max()]
df['Tenure_Bins'] = pd.cut(df['Tenure'],bins = bin_edges,include_lowest=True)
tenure_bins_grouped_churn = df.groupby('Tenure_Bins')['Churn'].value_counts()


# tenure_sum = 



# print("Gender Unique Values:", gender_unique)
# print("Contract Unique Values:", contract_unique)
# print("Internet Service Unique Values:", internet_service_unique)
# print("Tech Support Unique Values:", tech_support_unique)
# print("Churn Unique Values:", churn_unique)
# print("Number of Duplicate Rows:", len(no_duplicates))
# print('\n')
# print("Numeric values unique")
# print('\n')
# print('CustomerID Unique Values:', len(id_unique))
# print("CustomerID neg Values:", len(id_neg))
# print("Age neg Values:", len(age_neg))
# print("Tenure neg Values:", len(Tenure_neg))
# print("Monthly Charges neg Values:", len(monthly_charges_neg))
# print("Total Charges neg Values:", len(total_charges_neg))
# print(df["Churn"].value_counts())
# print(tenure_Grouped)
# print(Contract_grouped_churn)
# print(tenure_grouped_churn.head(1000))
# print(tenure_bins_grouped_churn)
 
df['InternetService'] = df['InternetService'].fillna('No Internet Service')
print(df.columns)
X =pd.DataFrame(df[['Tenure','MonthlyCharges','ContractType','InternetService','TechSupport']])
Y = pd.DataFrame(df[['Churn']])

dmy = pd.get_dummies(X[['ContractType','InternetService','TechSupport']],dtype=int)
print(dmy.columns)