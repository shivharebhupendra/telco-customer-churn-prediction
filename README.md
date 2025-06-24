# telco-customer-churn-prediction
End-to-end machine learning project to predict customer churn for a telecom company using Python, EDA, Logistic Regression, and Random Forest.

# 📊 Telco Customer Churn Prediction (End-to-End ML Project)

This is a complete machine learning project to predict customer churn in a telecom company. The goal is to identify customers who are likely to discontinue services based on usage patterns and demographic information.

---

## 🔍 Problem Statement

Customer churn is a major concern for subscription-based businesses. Retaining existing customers is more cost-effective than acquiring new ones. This project aims to build a predictive model that accurately identifies customers likely to churn, enabling proactive retention strategies.

---

## 📁 Project Structure
📦 Telco_Customer_Churn_Prediction
├── 01_DataLoading_and_EDA.ipynb
├── 02_Feature_Engineering_and_Preprocessing.ipynb
├── 03_Modeling_and_Evaluation.ipynb
├── WA_Fn-UseC_-Telco-Customer-Churn.xls # Original Dataset
├── cleaned_telco.xls # Cleaned Data
├── preprocessed_telco_churn.xls # Final Processed Data
├── best_logistic_regression.pkl # Saved Logistic Regression Model
├── best_random_forest.pkl # Saved Random Forest Model
└── README.md # Project Summary


---

## 🗃️ Dataset

- Source: [Kaggle - Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- Size: 7,043 customer records
- Features include:
  - Demographics: Gender, SeniorCitizen, Partner, Dependents
  - Services: Phone, Internet, Streaming, Tech support, etc.
  - Payment and Billing: MonthlyCharges, Contract, PaymentMethod
  - Target: `Churn` (Yes/No)

---

## ✅ Technologies Used

- **Language**: Python
- **IDE**: Jupyter Notebook
- **Libraries**:
  - `pandas`, `numpy` – Data handling
  - `matplotlib`, `seaborn` – Visualization
  - `scikit-learn` – Machine learning & model evaluation
  - `joblib` / `pickle` – Model saving

---

## 🧪 Step-by-Step Pipeline

### 📌 01. Data Loading & EDA
- Loaded the dataset and removed unnecessary columns (`customerID`)
- Explored data distributions, outliers, and correlations
- Visualized churn rate by various features

### 📌 02. Feature Engineering & Preprocessing
- Converted `TotalCharges` to numeric
- Encoded binary variables using `.map()` and multi-class with `get_dummies()`
- Scaled numerical features
- Created new features like:
  - `TotalServices` (count of services)
  - `AvgMonthlySpend`
  - `TenureGroup` (grouped customer loyalty)

### 📌 03. Modeling & Evaluation
- Trained Logistic Regression and Random Forest classifiers
- Handled class imbalance using `class_weight='balanced'`
- Used `GridSearchCV` for hyperparameter tuning
- Evaluated models using:
  - Accuracy, Precision, Recall, F1-score
  - Confusion Matrix
  - ROC-AUC Curve

---

## 📈 Model Performance (Post-Tuning)

| Model                | Accuracy | Precision (Churn) | Recall (Churn) | F1-Score | ROC-AUC |
|---------------------|----------|-------------------|----------------|----------|---------|
| Logistic Regression | 72%      | 0.49              | 79%            | 0.61     | **0.84** |
| Random Forest       | 76%      | 0.54              | 75%            | 0.63     | **0.82** |

---

## 🔍 Feature Importance

- **Top Influential Features**:
  - `Contract_Two year`
  - `MonthlyCharges`
  - `tenure`
  - `TechSupport_Yes`
  - `InternetService_Fiber optic`
- Logistic Regression and Random Forest both confirm these patterns.

---

## 💾 How to Run the Project

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/telco-churn-prediction.git
   cd telco-churn-prediction
2. Run each notebook step by step:
  - 01_DataLoading_and_EDA.ipynb
  - 02_Feature_Engineering_and_Preprocessing.ipynb
  - 03_Modeling_and_Evaluation.ipynb

🚀 Future Work
  - Deploy the model using Streamlit or Flask
  - Add SHAP/LIME for model explainability
  - Add dashboards or alerts for business use

🙏 Acknowledgements
- Dataset Source: Kaggle - Telco Customer Churn
- Inspired by real-world business challenges in telecom

📬 Contact
If you like this project or have any questions, feel free to connect:
GitHub: yourusername

LinkedIn: https://www.linkedin.com/in/bhupendra-shivhare-a8a02a25b/
