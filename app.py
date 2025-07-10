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

# github link
st.markdown("---")
st.markdown("[🔗 View Full Project on GitHub](https://github.com/shivharebhupendra/telco-customer-churn-prediction)")
