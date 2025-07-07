🤖 Claims Settlement Optimization System

This project builds an intelligent ML-based system that recommends optimal insurance claim settlements based on legal, customer, and risk-related factors. It classifies whether a claim should be settled or litigated and predicts the settlement amount if applicable.

----------------------------------------------------------
📌 Objective

Develop a model to automate and optimize insurance claim decisions by focusing on:
- Minimizing legal costs
- Maximizing customer satisfaction
- Reducing churn risk
- Identifying fraud probability
- Improving company profitability

----------------------------------------------------------
🧠 ML Models Used

Classification Task:           RandomForestClassifier
Regression (if Settle):        RandomForestRegressor
Tuning & Validation:           GridSearchCV, Cross-validation

----------------------------------------------------------
🛠️ Features Considered

- claim_type              → Auto / Health / Property / Life
- claim_amount            → Amount claimed
- customer_age            → Age of policyholder
- customer_tenure         → Relationship duration with company
- previous_claims_count   → Number of past claims
- legal_complexity        → Score from 1 (low) to 5 (high)
- estimated_legal_cost    → Projected legal expense
- customer_satisfaction   → Rating from 1 to 5
- fraud_risk_score        → Probability of fraud (0 to 1)
- churn_risk              → Customer attrition risk (0 to 1)
- region_risk_score       → Regional risk factor (0 to 1)

----------------------------------------------------------
🔄 Project Workflow

Claim Input
    ↓
Feature Encoding
    ↓
Classification → Settle or Litigate
                    ↓
         If Settle → Predict Settlement Amount

----------------------------------------------------------
✅ Accuracy & Optimization

- GridSearchCV for tuning
- 5-fold cross-validation for stability
- Random Forest for feature importance
- Robust to outliers and noise

----------------------------------------------------------
🧪 Sample Output

Predicted Recommendation:
Recommended Action: Settle
Recommended Settlement Amount: ₹152,300.75

----------------------------------------------------------
📁 Directory Structure

ClaimsSettlementSystem/
├── final_saved_claims_dataset.csv
├── claims_model_pipeline.ipynb
└── README_ClaimsOptimization.txt

----------------------------------------------------------
💻 How to Run

1. Clone the repository:
   git clone https://github.com/<your-username>/ClaimsSettlementSystem.git
   cd ClaimsSettlementSystem

2. Install dependencies:
   pip install pandas numpy scikit-learn matplotlib seaborn

3. Run the notebook or script:
   - Open claims_model_pipeline.ipynb using Jupyter Notebook
   - OR convert it to a .py file and run in terminal

----------------------------------------------------------
📦 Requirements

- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn

You can also use:
   pip install -r requirements.txt

----------------------------------------------------------
🚀 Future Enhancements

- Convert to a web app using Streamlit
- Add dashboard for claim monitoring
- Integrate with insurance APIs
- Enhance fraud detection using NLP + Deep Learning

----------------------------------------------------------
👤 Author

Built by: Shashidhar
Email: your-2210030031cse@gmail.com


----------------------------------------------------------
📜 License

MIT License – See LICENSE file for more details.
