import pandas as pd

# Load your risk-scored dataset
file_path = "C:/Users/Khemb/OneDrive - Teknikally Speaking/Insurance_Analytics/data/processed/Risk_Scored_Insurance_Data.csv"
data = pd.read_csv(file_path)

# Create multiple fake high-claim records for the same customer to simulate fraud
fraud_records = pd.DataFrame({
    'customer_id': ['FAKE_CUST_999'] * 5,
    'policy_id': ['FAKE_POLICY_999'] * 5,
    'claim_amount': [100000] * 5,  # Extremely high claims
    'policy_premium': [500] * 5,
    'risk_score': [0.9] * 5,
    'processing_days': [1] * 5,
    'claim_to_premium_ratio': [200] * 5,
    'is_high_risk': [1] * 5,
    'processing_efficiency': [100000] * 5,
    'claim_id': ['CL_FAKE_001', 'CL_FAKE_002', 'CL_FAKE_003', 'CL_FAKE_004', 'CL_FAKE_005']
})

# Append these fake fraud records to your dataset
data = pd.concat([data, fraud_records], ignore_index=True)

# Save the updated dataset for re-scoring
output_path = "C:/Users/Khemb/OneDrive - Teknikally Speaking/Insurance_Analytics/data/processed/Risk_Scored_Insurance_Data_with_FakeFraud.csv"
data.to_csv(output_path, index=False)

print("✅ Fake fraudulent claims added for validation. File saved to:")
print(output_path)