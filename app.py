import streamlit as st
import pickle

model = pickle.load(open("model.pkl","rb"))
vectorizer = pickle.load(open("vectorizer.pkl","rb"))

st.title("Fake News Detector")

input_text = st.text_area("Enter News Article")

if st.button("Check News"):

    vector = vectorizer.transform([input_text])
    prediction = model.predict(vector)

    if prediction == 0:
        st.write("Fake News ❌")
    else:
        st.write("Real News ✅")
