import pandas as pd
import sys

# Load the dataset with injected fake fraud case
file_path = "C:/Users/Khemb/OneDrive - Teknikally Speaking/Insurance_Analytics/data/processed/Risk_Scored_Insurance_Data_with_FakeFraud.csv"
data = pd.read_csv(file_path)

# Validate required columns
required_columns = ['customer_id', 'claim_id', 'claim_amount']
missing_columns = [col for col in required_columns if col not in data.columns]
if missing_columns:
    print(f"❌ Missing required columns: {', '.join(missing_columns)}")
    sys.exit(1)
else:
    print("✅ All required columns are present. Proceeding with risk scoring...")

# 1. Claim Frequency per Customer
data['claim_frequency'] = data.groupby('customer_id')['claim_id'].transform('count')

# 2. Total Claim Amount per Customer
data['total_claim_amount'] = data.groupby('customer_id')['claim_amount'].transform('sum')

# 3. High-Claim Threshold (95th percentile)
high_claim_threshold = data['claim_amount'].quantile(0.95)
data['high_claim_flag'] = data['claim_amount'] > high_claim_threshold

# 4. Fraud Risk Flag - High claim + High frequency
data['fraud_risk_flag'] = (data['high_claim_flag']) & (data['claim_frequency'] > 3)

# Preview flagged results to verify FAKE_CUST_999 is flagged
flagged = data[data['fraud_risk_flag'] == True]
print("\n📋 Fraud Risk Flagged Records Preview:")
print(flagged[['customer_id', 'claim_id', 'claim_amount', 'claim_frequency', 'high_claim_flag', 'fraud_risk_flag']])

# Save the flagged results
output_path = "C:/Users/Khemb/OneDrive - Teknikally Speaking/Insurance_Analytics/data/processed/Risk_Scored_Insurance_Data_FraudChecked.csv"
data.to_csv(output_path, index=False)

print("\n✅ Risk scoring and fraud detection complete. File saved to:")
print(output_path)
