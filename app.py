import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Download required nltk datasets
nltk.download('punkt')
nltk.download('stopwords')

ps = PorterStemmer()

# Store stopwords and punctuation in variables
stop_words = set(stopwords.words('english'))
punctuations = set(string.punctuation)

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    # Remove non-alphanumeric characters
    text = [i for i in text if i.isalnum()]

    # Remove stopwords and punctuation
    text = [i for i in text if i not in stop_words and i not in punctuations]

    # Apply stemming
    text = [ps.stem(i) for i in text]

    return " ".join(text)

# Load the pre-trained models
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# Streamlit UI
st.title("Email/SMS Spam Classifier")
input_sms = st.text_area("Enter the message")

if st.button('Predict'):
    transformed_sms = transform_text(input_sms)
    vector_input = tfidf.transform([transformed_sms])
    result = model.predict(vector_input)[0]

    st.header("Spam" if result == 1 else "Not Spam")
