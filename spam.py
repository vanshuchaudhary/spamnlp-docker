import streamlit as st
import requests
import time

st.set_page_config(page_title="Spam Detector", page_icon="🚨")

st.title("NLP Based Spam Detection App")
st.write("UI loaded successfully")

your_message = st.text_input("Enter message")

if st.button("Predict"):
    if your_message.strip() == "":
        st.warning("Please enter a message")
    else:
        # 1. Show a loading spinner so the user knows to wait for the wake-up
        with st.spinner("Waking up the API... This may take a minute on the Free Tier."):
            try:
                response = requests.post(
                    "https://spamnlp-api-flask.onrender.com/predict", # Make sure /predict is at the end!
                    json={"message": your_message},
                    timeout=60 # Give it 60 seconds to wake up
                )
                
                if response.status_code == 200:
                    result = response.json()
                    
                    st.write("Spam Probability:", round(result["spam_probability"], 4))

                    prob = result.get("spam_probability", 0)
                    pred = result.get("prediction", 0)

                    st.write(f"Spam Probability: {prob:.4f}")

# Fix: Check if prediction is 1 (as int or string) OR if probability is > 0.5
                    if str(pred) == "1" or prob >= 0.5:
                        st.error("🚨 SPAM MESSAGE")
                    else:
                        st.success("✅ HAM MESSAGE")
                else:
                    st.error(f"API Error: Received status code {response.status_code}")

            except requests.exceptions.ReadTimeout:
                st.error("The API is taking too long to wake up. Please wait 10 seconds and click Predict again.")
            except Exception as e:
                st.error(f"Connection Error: {e}")

# Background styling
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
