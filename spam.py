import streamlit as st
import joblib
import pandas as pd
import numpy as np 
import requests

st.title("NLP Based Spam Detection App")
st.write("UI loaded successfully")

your_message = st.text_input("Enter message")

if st.button("Predict"):
    if your_message.strip() == "":
        st.warning("Please enter a message")
    else:
        response = requests.post(
            "https://spamnlp-api-flask.onrender.com",
            json={"message": your_message}
        )

        result = response.json()

        st.write("Spam Probability:",  result["spam_probability"])

        if result["prediction"] == 1:
            st.error("🚨 SPAM MESSAGE")
        else:
            st.success("✅ HAM MESSAGE")

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True

)
