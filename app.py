{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "070126c3-49d7-4bdf-a3f2-e006f35c7ce9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# import libraries\n",
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "import warnings\n",
    "warnings.filterwarnings(\"ignore\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "a40c3e4f-2243-4a12-9238-cf8b8baf8567",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# set title and layout\n",
    "st.set_page_config(page_title=\"Telco Customer Churn Prediction\", layout=\"wide\")\n",
    "st.title(\"Telco Customer Churn Prediction App\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "f2aeb8b4-129c-45a7-9b52-acb71a367582",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-07-10 07:26:36.489 No runtime found, using MemoryCacheStorageManager\n"
     ]
    }
   ],
   "source": [
    "# load data\n",
    "@st.cache_data\n",
    "def load_data():\n",
    "    df = pd.read_csv(\"WA_Fn-UseC_-Telco-Customer-Churn.csv\")\n",
    "    return df\n",
    "\n",
    "df = load_data()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "3e7b0bea-ae63-4100-be40-37cc6cbbfe66",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# show raw data\n",
    "st.subheader(\"Raw Data\")\n",
    "st.dataframe(df.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "51ca18a8-a56e-402c-af6c-e13f3d447ef4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# churn distribution plot\n",
    "fig1, ax1 = plt.subplots()\n",
    "sns.countplot(x=\"Churn\", data=df, ax=ax1)\n",
    "st.pyplot(fig1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "f91ea8dd-9984-42a7-88a7-cb3060bc080a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# churn by contract type\n",
    "st.subheader(\"Churn by Contract Type\")\n",
    "fig2, ax2 = plt.subplots()\n",
    "sns.countplot(x=\"Contract\", hue=\"Churn\", data=df, ax=ax2)\n",
    "st.pyplot(fig2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "1d4864a2-51c8-419e-aa56-b6a9acc385e3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# github link\n",
    "st.markdown(\"---\")\n",
    "st.markdown(\"[View Full Project on GitHub] (https://github.com/shivharebhupendra/telco-customer-churn-prediction)\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1e7f4dc5-f531-422e-85a4-6bb7508045a3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
