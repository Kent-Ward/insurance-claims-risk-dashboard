import pandas as pd

# Load your feature engineered dataset
file_path = "C:/Users/Khemb/OneDrive - Teknikally Speaking/Insurance_Analytics/data/processed/Feature_Engineered_Insurance_Data.csv"
data = pd.read_csv(file_path)

# Create synthetic claim IDs like CL101, CL102, etc.
start_number = 101
data['claim_id'] = ['CL' + str(i) for i in range(start_number, start_number + len(data))]

# Preview the last 5 claim IDs to confirm
print("📋 Preview of New Synthetic Claim IDs (last 5 rows):")
print(data[['claim_id']].tail())

# Save the updated data
output_path = "C:/Users/Khemb/OneDrive - Teknikally Speaking/Insurance_Analytics/data/processed/Feature_Engineered_Insurance_Data_with_ClaimID.csv"
data.to_csv(output_path, index=False)

print("\n✅ Synthetic Claim IDs (CL101, CL102, ...) added. File saved to:")
print(output_path)

