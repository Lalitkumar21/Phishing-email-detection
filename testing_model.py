import joblib
import sys
import streamlit as st

model = joblib.load('phishing_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

st.title('Phishing Email Detector')

st.write("Choose how to provide the email content:")

input_method = st.radio(
    "Select input method:",
    ('Paste Email Text', 'Upload .txt File')
)

email_text = ''

if input_method =='Paste Email Text':
    email_text = st.text_area("Paste the email content below: ")
elif input_method =='Upload .txt File':
    uploaded_file = st.file_uploader('Choose a .txt file', type='txt')
    if uploaded_file is not None:
        email_text = uploaded_file.read().decode('utf-8')

if st.button('Check Email'):
    if email_text.strip()=='':
        st.warning("Please provide email content")
    else:
        vectorizer_input = vectorizer.transform([email_text])
        prediction = model.predict(vectorizer_input)
        if prediction[0]==1:
            st.error("This is a Phishing email")
        else:
            st.success("This email is safe")