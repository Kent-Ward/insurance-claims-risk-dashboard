import pandas as pd

# Load the cleaned dataset
file_path = "C:/Users/Khemb/OneDrive - Teknikally Speaking/Insurance_Analytics/data/processed/Cleaned_Merged_Insurance_Data.csv"
data = pd.read_csv(file_path)

# Feature Engineering

# 1. Claim to Premium Ratio
data['claim_to_premium_ratio'] = data['claim_amount'] / data['policy_premium']

# 2. High Risk Flag
data['is_high_risk'] = data['risk_score'].apply(lambda x: 1 if x > 0.7 else 0)

# 3. Processing Efficiency
data['processing_efficiency'] = data['claim_amount'] / data['processing_days']

# Save the updated dataset
output_path = "C:/Users/Khemb/OneDrive - Teknikally Speaking/Insurance_Analytics/data/processed/Feature_Engineered_Insurance_Data.csv"
data.to_csv(output_path, index=False)

print("✅ Feature engineering complete. File saved to:")
print(output_path)
