# import libraries
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")

# set title and layout
st.set_page_config(page_title="Telco Customer Churn Prediction", layout="wide")
st.title("📊 Telco Customer Churn Prediction App")

# load data
@st.cache_data
def load_data():
    df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
    return df

df = load_data()

# show raw data
st.subheader("🔍 Raw Data")
st.dataframe(df.head())

# churn distribution plot
st.subheader("📌 Churn Distribution")
fig1, ax1 = plt.subplots()
sns.countplot(x="Churn", data=df, ax=ax1)
st.pyplot(fig1)

# churn by contract type
st.subheader("📊 Churn by Contract Type")
fig2, ax2 = plt.subplots()
sns.countplot(x="Contract", hue="Churn", data=df, ax=ax2)
st.pyplot(fig2)


st.markdown("---")
st.header("🔮 Predict Customer Churn")
import joblib

# Load model
model = joblib.load("best_random_forest.pkl")

# Define feature columns (based on your preprocessed data)
feature_columns = [
    'gender',
    'SeniorCitizen',
    'Partner',
    'Dependents',
    'tenure',
    'PhoneService',
    'PaperlessBilling',
    'MonthlyCharges',
    'TotalCharges',
    'MultipleLines_No phone service',
    'MultipleLines_Yes',
    'InternetService_Fiber optic',
    'InternetService_No',
    'OnlineSecurity_No internet service',
    'OnlineSecurity_Yes',
    'OnlineBackup_No internet service',
    'OnlineBackup_Yes',
    'DeviceProtection_No internet service',
    'DeviceProtection_Yes',
    'TechSupport_No internet service',
    'TechSupport_Yes',
    'StreamingTV_No internet service',
    'StreamingTV_Yes',
    'StreamingMovies_No internet service',
    'StreamingMovies_Yes',
    'Contract_One year',
    'Contract_Two year',
    'PaymentMethod_Credit card (automatic)',
    'PaymentMethod_Electronic check',
    'PaymentMethod_Mailed check'
]

# Title
st.set_page_config(page_title="Telco Churn Predictor", layout="centered")
st.title("📊 Telco Customer Churn Prediction")

# User Inputs
gender = st.selectbox("Gender", [1, 0])
senior = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.slider("Tenure (months)", 0, 72, 12)
phone_service = st.selectbox("Phone Service", ["Yes", "No"])
paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
monthly = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
total = st.number_input("Total Charges", 0.0, 10000.0, 3000.0)

# Additional One-Hot Features
multi_lines = st.selectbox("Multiple Lines", ["No phone service", "Yes", "No"])
internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
online_sec = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
online_bak = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
device_protect = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
stream_tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
stream_movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
payment = st.selectbox("Payment Method", [
    "Electronic check",
    "Mailed check",
    "Bank transfer (automatic)",
    "Credit card (automatic)"
])

# Build feature dict
input_dict = {
    'gender': gender,
    'SeniorCitizen': senior,
    'Partner': partner,
    'Dependents': dependents,
    'tenure': tenure,
    'PhoneService': phone_service,
    'PaperlessBilling': paperless,
    'MonthlyCharges': monthly,
    'TotalCharges': total
}

# One-hot encode manually to match expected features
for col in feature_columns:
    if col not in input_dict:
        input_dict[col] = 0

# Set one-hot values
input_dict[f'MultipleLines_{multi_lines}'] = 1 if f'MultipleLines_{multi_lines}' in feature_columns else 0
input_dict[f'InternetService_{internet}'] = 1 if f'InternetService_{internet}' in feature_columns else 0
input_dict[f'OnlineSecurity_{online_sec}'] = 1 if f'OnlineSecurity_{online_sec}' in feature_columns else 0
input_dict[f'OnlineBackup_{online_bak}'] = 1 if f'OnlineBackup_{online_bak}' in feature_columns else 0
input_dict[f'DeviceProtection_{device_protect}'] = 1 if f'DeviceProtection_{device_protect}' in feature_columns else 0
input_dict[f'TechSupport_{tech_support}'] = 1 if f'TechSupport_{tech_support}' in feature_columns else 0
input_dict[f'StreamingTV_{stream_tv}'] = 1 if f'StreamingTV_{stream_tv}' in feature_columns else 0
input_dict[f'StreamingMovies_{stream_movies}'] = 1 if f'StreamingMovies_{stream_movies}' in feature_columns else 0

if contract == "One year":
    input_dict['Contract_One year'] = 1
elif contract == "Two year":
    input_dict['Contract_Two year'] = 1

if payment == "Credit card (automatic)":
    input_dict['PaymentMethod_Credit card (automatic)'] = 1
elif payment == "Electronic check":
    input_dict['PaymentMethod_Electronic check'] = 1
elif payment == "Mailed check":
    input_dict['PaymentMethod_Mailed check'] = 1

# Prepare input for model
input_df = pd.DataFrame([input_dict])[feature_columns]

# Predict
if st.button("Predict Churn"):
    prediction = model.predict(input_df)[0]
    if prediction == 1:
        st.error("⚠️ The customer is likely to churn.")
    else:
        st.success("✅ The customer is not likely to churn.")
# github link     
st.markdown("---")
st.markdown("[🔗 View Full Project on GitHub](https://github.com/shivharebhupendra/telco-customer-churn-prediction)")
