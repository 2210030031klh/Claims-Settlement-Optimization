import pandas as pd
import numpy as np
import random
import os

# Set random seed for reproducibility
random.seed(42)
np.random.seed(42)

# Number of samples
n_samples = 500
claim_types = ["Auto", "Health", "Property", "Life"]

# Function to generate dataset
def generate_final_claims_dataset(n):
    data = []
    for i in range(n):
        claim_id = f"C{i+1:05d}"
        claim_type = random.choice(claim_types)
        claim_amount = np.random.randint(10000, 500000)
        customer_age = np.random.randint(18, 80)
        customer_tenure = round(np.random.uniform(0.1, 15), 1)
        previous_claims_count = np.random.poisson(1)
        legal_complexity = np.random.randint(1, 6)
        estimated_legal_cost = round(np.random.uniform(10000, 150000), 2)
        customer_satisfaction = np.random.randint(1, 6)
        fraud_risk_score = round(np.random.beta(2, 5), 2)

        # Churn Risk Logic
        if customer_tenure < 1.5 and customer_satisfaction <= 2:
            churn_risk = round(np.random.uniform(0.7, 1.0), 2)
        elif customer_tenure < 3 and customer_satisfaction <= 3:
            churn_risk = round(np.random.uniform(0.5, 0.8), 2)
        elif customer_tenure > 5 and customer_satisfaction >= 4:
            churn_risk = round(np.random.uniform(0.0, 0.3), 2)
        else:
            churn_risk = round(np.random.uniform(0.3, 0.7), 2)

        # Region Risk Logic
        if claim_type in ["Auto", "Property"] and legal_complexity >= 4:
            region_risk_score = round(np.random.uniform(0.6, 1.0), 2)
        elif claim_type in ["Health", "Life"] and legal_complexity <= 2:
            region_risk_score = round(np.random.uniform(0.0, 0.4), 2)
        else:
            region_risk_score = round(np.random.uniform(0.3, 0.7), 2)

        # Recommended Action Logic
        if (
            estimated_legal_cost > 0.4 * claim_amount or
            (fraud_risk_score > 0.65 and churn_risk > 0.5) or
            (customer_satisfaction >= 4 and churn_risk > 0.6)
        ):
            recommended_action = "Settle"
            recommended_settlement = round(claim_amount * np.random.uniform(0.6, 0.9), 2)
        else:
            recommended_action = "Litigate"
            recommended_settlement = 0.0

        data.append([
            claim_id, claim_type, claim_amount, customer_age, customer_tenure,
            previous_claims_count, legal_complexity, estimated_legal_cost,
            customer_satisfaction, fraud_risk_score, churn_risk, region_risk_score,
            recommended_action, recommended_settlement
        ])

    columns = [
        "claim_id", "claim_type", "claim_amount", "customer_age", "customer_tenure",
        "previous_claims_count", "legal_complexity", "estimated_legal_cost",
        "customer_satisfaction", "fraud_risk_score", "churn_risk", "region_risk_score",
        "recommended_action", "recommended_settlement"
    ]

    return pd.DataFrame(data, columns=columns)

# Generate dataset
df = generate_final_claims_dataset(n_samples)

# Save to Desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "final_saved_claims_dataset.csv")
df.to_csv(desktop_path, index=False)

print(f"✅ Dataset saved to Desktop: {desktop_path}")
