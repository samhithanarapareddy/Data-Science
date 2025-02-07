# cook your dish here
import pandas as pd
import numpy as np

# Load dataset
data = pd.read_csv('customer_data.csv')

# Check for duplicates
duplicates = data.duplicated().sum()
print(f'Total Duplicates: {duplicates}')

# Remove duplicates
data = data.drop_duplicates()

# Check for missing values
missing_values = data.isnull().sum()
print('Missing Values:\n', missing_values)

# Fill missing values (example: fill missing age with median age)
data['age'].fillna(data['age'].median(), inplace=True)

# Validate email addresses
valid_emails = data['email'].apply(lambda x: pd.notnull(x) and '@' in x)
print(f'Invalid Emails: {len(data) - valid_emails.sum()}')

# Validate phone numbers (example: must be 10 digits)
valid_phones = data['phone'].apply(lambda x: pd.notnull(x) and len(str(x)) == 10)
print(f'Invalid Phone Numbers: {len(data) - valid_phones.sum()}')

# Save cleaned data
data.to_csv('cleaned_customer_data.csv', index=False)
