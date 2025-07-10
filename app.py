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

# Form inputs
gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Partner", ["Yes", "No"])
tenure = st.slider("Tenure (months)", 0, 72, 12)
monthly = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])

# Manual one-hot encoding
input_data = {
    'gender': gender,
    'SeniorCitizen': senior,
    'Partner': partner,
    'tenure': tenure,
    'MonthlyCharges': monthly,
    'Contract_One year': 1 if contract == "One year" else 0,
    'Contract_Two year': 1 if contract == "Two year" else 0
}

# Fill missing dummy columns (if model expects them)
all_features = [
    'gender', 'SeniorCitizen', 'Partner', 'tenure', 'MonthlyCharges',
    'Contract_One year', 'Contract_Two year'
]
for col in all_features:
    if col not in input_data:
        input_data[col] = 0

input_df = pd.DataFrame([input_data])

# Load model
import joblib
model = joblib.load("best_random_forest.pkl")

# Predict
if st.button("Predict Churn"):
    pred = model.predict(input_df)[0]
    if pred == 1:
        st.error("⚠️ This customer is likely to churn.")
    else:
        st.success("✅ This customer is not likely to churn.")

# github link     
st.markdown("---")
st.markdown("[🔗 View Full Project on GitHub](https://github.com/shivharebhupendra/telco-customer-churn-prediction)")
