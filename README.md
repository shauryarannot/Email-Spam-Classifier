# Email Spam Classifier

## Overview
This project is an **Email Spam Classifier** built using **machine learning** and deployed as a **web application** using **Streamlit**. The model classifies emails as **Spam** or **Not Spam** based on text content.

## Features
- **Pretrained Machine Learning Model** for spam classification
- **User-friendly Web Interface** powered by Streamlit
- **Real-time Email Classification**
- **Interactive and Lightweight Design**

## Installation
### Prerequisites
Ensure you have the following installed:
- Python (>=3.7)
- pip (Python package manager)

### Clone the Repository
```bash
git clone https://github.com/your-username/email-spam-classifier.git
cd email-spam-classifier
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage
Run the Streamlit app using:
```bash
streamlit run app.py
```
This will open the application in your web browser.

## Model Details
The classifier is built using:
- **TF-IDF Vectorization** for text processing
- **Naive Bayes / Logistic Regression / Random Forest** (Choose based on performance)

## Deployment
The application is deployed using **Streamlit Cloud / Heroku / AWS**. You can access it live [here](your-deployment-link).

## File Structure
```
email-spam-classifier/
│-- app.py                 # Main application file
│-- model.pkl              # Trained ML model
│-- vectorizer.pkl         # TF-IDF Vectorizer
│-- requirements.txt       # Dependencies
│-- README.md              # Project documentation
```

## Contributing
Feel free to contribute! Fork the repository, create a branch, and submit a pull request.

## License
This project is licensed under the MIT License.
