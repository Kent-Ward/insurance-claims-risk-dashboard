# insurance_data_cleaning.py

import pandas as pd

# Step 1: Load the datasets using your actual file paths
claims_data = pd.read_csv('C:/Users/Khemb/OneDrive - Teknikally Speaking/Insurance_Analytics/data/raw/Insurance_Claims_Data.csv')
customers_data = pd.read_csv('C:/Users/Khemb/OneDrive - Teknikally Speaking/Insurance_Analytics/data/raw/Insurance_Customers_Data.csv')

# Step 2: Preview the first few rows of each dataset
print("Claims Data Preview:")
print(claims_data.head())

print("\nCustomers Data Preview:")
print(customers_data.head())

# Step 3: Check for missing values
print("\nMissing values in Claims Data:")
print(claims_data.isnull().sum())

print("\nMissing values in Customers Data:")
print(customers_data.isnull().sum())

# Step 4: Check data types
print("\nData types in Claims Data:")
print(claims_data.dtypes)

print("\nData types in Customers Data:")
print(customers_data.dtypes)

# Step 5: Remove any duplicate rows
claims_data = claims_data.drop_duplicates()
customers_data = customers_data.drop_duplicates()

# Step 6: Standardize column names to lowercase
claims_data.columns = claims_data.columns.str.lower()
customers_data.columns = customers_data.columns.str.lower()

# Step 7: Merge the datasets on 'customer_id'
merged_data = pd.merge(claims_data, customers_data, on='customer_id', how='inner')

# Step 8: Preview the merged dataset
print("\nCleaned and Merged Data Preview:")
print(merged_data.head())

# Step 9: Save the cleaned dataset to a new CSV file
merged_data.to_csv('C:/Users/Khemb/OneDrive - Teknikally Speaking/Insurance_Analytics/data/raw/Cleaned_Merged_Insurance_Data.csv', index=False)
print("\nCleaned dataset saved as 'Cleaned_Merged_Insurance_Data.csv'")

