import pandas as pd

# Load the fraud-checked data
file_path = "C:/Users/Khemb/OneDrive - Teknikally Speaking/Insurance_Analytics/data/processed/Risk_Scored_Insurance_Data_FraudChecked.csv"
data = pd.read_csv(file_path)

# Select only relevant columns for Tableau
tableau_ready = data[[
    'customer_id',
    'claim_id',
    'claim_amount',
    'claim_frequency',
    'high_claim_flag',
    'fraud_risk_flag'
]]

# Save to a clean export file
output_path = "C:/Users/Khemb/OneDrive - Teknikally Speaking/Insurance_Analytics/data/final/Tableau_Insurance_Claims_Data.csv"
tableau_ready.to_csv(output_path, index=False)

print("✅ Tableau export created. File saved to:")
print(output_path)
