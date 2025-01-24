import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load('spam_classifier_model.pkl')
tfidf = joblib.load('tfidf_vectorizer.pkl')

st.title("Spam Email Classifier")

# Input from user
message = st.text_area("Enter the email/message text:")

if st.button("Classify"):
    if message.strip() != "":
        # Preprocess and predict
        message_tfidf = tfidf.transform([message])
        prediction = model.predict(message_tfidf)
        result = "Spam" if prediction[0] == 1 else "Not Spam"
        st.write(f"Prediction: {result}")
    else:
        st.write("Please enter a valid message!")
