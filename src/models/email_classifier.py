import os
import kagglehub
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Download the Enron Email Dataset
path = kagglehub.dataset_download("wcukierski/enron-email-dataset")
print("Path to dataset files:", path)

# Function to load and format the Enron Email Dataset from a CSV file
def load_enron_dataset_from_csv(csv_path):
    emails = []
    labels = []
    df = pd.read_csv(csv_path)
    for index, row in df.iterrows():
        emails.append(row['message'])
        labels.append(row['label'])
    return emails, labels

# Path to the CSV file
csv_path = os.path.join(path, 'emails.csv')

# Load the dataset
emails, labels = load_enron_dataset_from_csv(csv_path)

# Print debug information
print(f"Number of emails: {len(emails)}")
print(f"First email content: {emails[0] if emails else 'No emails found'}")

# Check if emails list is empty
if not emails:
    raise ValueError("No valid emails found in the dataset.")

# Vectorize the email content
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(emails)

# Train a Naive Bayes classifier
model = MultinomialNB()
model.fit(X, labels)

# Save the model and vectorizer
joblib.dump(model, 'email_classifier.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

def classify_email(content):
    """
    Classify the given email content as spam or ham.

    Args:
        content (str): The content of the email to classify.

    Returns:
        str: The classification result ('spam' or 'ham').
    """
    model = joblib.load('email_classifier.pkl')
    vectorizer = joblib.load('vectorizer.pkl')
    X = vectorizer.transform([content])
    prediction = model.predict(X)
    return prediction[0]

# Use case
if __name__ == "__main__":
    test_email = "This is a test email content."
    print("Classification:", classify_email(test_email))